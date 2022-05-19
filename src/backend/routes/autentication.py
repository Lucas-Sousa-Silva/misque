from datetime import timedelta
from typing import Union

from asyncpg import Connection, Pool
from dependencies.dependencies import get_pool
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from models.testingmodels import Conta
from modules.accounting.normal_user_accounting import (conta_exists,
                                                       get_conta_by_nick)
from pydantic import BaseModel
from security.security import (ACCESS_TOKEN_EXPIRE_MINUTES,  # verify_password,
                               authenticate_user, create_access_token,
                               get_username, get_current_user)

autentication = APIRouter(tags=["autentication"])


@autentication.get("/users/me")
async def get_yourself(
    _current_user: Conta = Depends(get_current_user)
):
    return _current_user

@autentication.post("/token")
async def login(
    pool: Pool = Depends(get_pool),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
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

