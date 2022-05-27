from datetime import timedelta

from asyncpg import Pool
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from dependencies.dependencies import get_pool
from models.testingmodels import ContaComHash
from security.security import (authenticate_user, create_access_token,
                               generate_hash, get_current_user)

autentication = APIRouter(tags=["autentication"])

@autentication.get("/gen_hash")
async def gen_hash(
    to_hash: str
):
    return generate_hash(to_hash)

@autentication.get("/users/me")
async def get_yourself(
    current_user: ContaComHash = Depends(get_current_user)
):
    return current_user

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

