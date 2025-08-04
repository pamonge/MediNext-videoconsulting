from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTerror
import os

oauth2_scheme = OAuth2PasswordBearer(token='/auth/token')
SECRET_KEY = os.getenv('SECRET_KEY', 'supersecreto')
ALGORITHM = 'HS256'

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {'username': payload.get('sub'), 'role': payload.get('role')} # role está en profile_service
    except JWTerror:
        raise HTTPException(status_code=401, detail='Token invalido')