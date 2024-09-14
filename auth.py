from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from config import get_settings,Settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para verificar o token
def verify_token(token: str = Depends(oauth2_scheme),settings: Annotated[Settings, Depends(get_settings)] = None):
    try:
        is_auth = token == settings.api_key
        if(not is_auth):
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
            )
        
        return is_auth
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )