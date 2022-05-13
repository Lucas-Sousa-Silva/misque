from fastapi import APIRouter, Depends
from fastapi.security import(
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nick : str
    password : str 

usuarios = [
    Usuario(nick="josisvaldo", password="vidaloka"),
    Usuario(nick="negueba", password="acai"),
]

autentication = APIRouter(tags=["autentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@autentication.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return form_data