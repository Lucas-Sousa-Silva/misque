""" Module for storage of security globals (Singleton(I hope that I don't define again these funcions )) """
from datetime import datetime, timedelta
from pydantic import BaseModel

from asyncpg import Connection, Pool
from jose import JWTError, jwt
from modules.accounting.normal_user_accounting import get_conta_com_hash
from dependencies.dependencies import get_pool
from models.testingmodels import ContaComHash
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "20735005b378d3041882a3d6a6ff09e958d5f1cd8e5c09acd2b1ae88fd3559ac"
ALGORITHM = "HS512"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    username: str | None = None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_hash(pwd):
    return pwd_context.hash(pwd)

def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_username(token:str):
    # Get the token descryptographed to a dict
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    return username

async def authenticate_user(connection: Connection, username: str, password:str) -> ContaComHash | bool:
    user = await get_conta_com_hash(connection, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(
    pool: Pool = Depends(get_pool),
    token: str = Depends(oauth2_scheme)
)-> ContaComHash:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        username = get_username(token)
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    async with pool.acquire() as connection:
        conta = await get_conta_com_hash(connection, nick=token_data.username)

    if conta is None:
        raise credentials_exception

    return conta