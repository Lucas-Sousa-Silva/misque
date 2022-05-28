from datetime import timedelta

from asyncpg import Pool
from fastapi import APIRouter, Depends, HTTPException, status, Path
from fastapi.security import OAuth2PasswordRequestForm

from dependencies.dependencies import get_pool
from models.testingmodels import ContaComHash, Conta
from modules.accounting.normal_user_accounting import criar_conta
from security.security import (authenticate_user, create_access_token,
                               generate_hash, get_current_user)

autentication = APIRouter(tags=["autentication"])


################################################################################
@autentication.post("/users" ,status_code=status.HTTP_201_CREATED)
async def create_user(
    conta : Conta,
    senha : str,
    pool: Pool = Depends(get_pool),
):
    """ Creates a new user. """
    async with pool.acquire() as connection:
        try:
            await criar_conta(connection, conta, generate_hash(senha))
        except ValueError as ve:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="Conta with this nick already exists"
            )
    return {"detail": "Conta created sucessfully."}


################################################################################
@autentication.get("/users/me")
async def get_yourself(
    current_user: ContaComHash = Depends(get_current_user)
):
    return current_user


################################################################################
@autentication.get("/gen_hash")
async def gen_hash(
    to_hash: str
):
    return generate_hash(to_hash)



################################################################################
@autentication.post("/token")
async def login(
    pool: Pool = Depends(get_pool),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    # The user must generate another token each hour
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    username = form_data.username
    password = form_data.password
    async with pool.acquire() as connection:
        conta = await authenticate_user(connection, username, password)
        if not conta:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password."
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":conta.nick}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

