from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer


autentication = APIRouter(tags=["autentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@autentication.get("/token",)
async def get_token(
    token: str = Depends(oauth2_scheme)
):
    return {"token":token}