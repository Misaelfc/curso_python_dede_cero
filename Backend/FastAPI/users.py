### Users API ###

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str    
    age: int
    
users_list = [
    User(id = 1, name ="Misael", surname = "Flores", url = "https://abraham.dev", age = 33),
    User(id = 2, name = "Brais", surname = "Moure", url = "https://moure.dev", age = 33),
    User(id = 3, name = "Brais", surname = "Dev", url = "https://abrahamdev.com", age = 20)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Misael", "surname": "Flores", "url": "https://abraham.dev", "age": 33},
            {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 33},
            {"name": "Brais", "surname": "Dev", "url": "https://abrahamdev.com", "age": 20}]
    
@app.get("/users") # get es para leer datos
async def get_users():
    return users_list

#Path

@app.get("/user/{id}")
async def get_user(id: int):
    return search_user(id)

# Query

@app.get("/user/")
async def user(id: int):
    return search_user(id)

# Post

@app.post("/user/", response_model=User, status_code=201) 
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="EL usuario ya existe")
        
    users_list.append(user)
    return user
    

@app.put("/user/")
async def update_user(user: User):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error": "No se ha actualizado el usuario."}
    
    return user
    
@app.delete("/user/{id}")
async def user(id: int):

    found = False    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario."}
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}
    
