# Instalar libreria de criptografia pip3 install "python-jose[cryptography]"
# También se instala esta libreria pip3 install "passlib[bcrypt]"

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "5a81b4c0aee97b29d1ce9a4f361b859eb0a6446e373c2a9bc86021f9c9ed2cf4"

router = APIRouter(prefix="/jwtauth", 
                    tags= ["jwtauth"], 
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    surname: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str
    
users_db ={
    "abrahamdev": {
    "username": "abrahamdev",
    "full_name": "Misael Flores",
    "surname": "Flores",
    "email": "aflorescastrejon@gmail.com",
    "disabled": False,
    "password": "$2a$12$tBxSlCZO/rpOePwCJXPy2.DZap.0q7RJrYuljDQamwP7SfjDrx1pS"  
    },
    "abrahamdev2": {
    "username": "abrahamdev2",
    "full_name": "Misael Flores 2",
    "surname": "Flores",
    "email": "aflorescastrejon2@gmail.com",
    "disabled": True, 
    "password": "$2a$12$iuOCtHUWyslxFSYbfwEuzO.3YogyzkbuKbU4Dis5R2j5oNU5hYt2y"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    return None

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    return None

async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)    

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
        
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
        
    user = search_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    acces_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
        
    return {"access_token": jwt.encode(acces_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
