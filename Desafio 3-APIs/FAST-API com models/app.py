from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db:List[User] = [
    User(id=UUID("57347a82-1743-4ed4-9c13-784b871a0d2e"),
         first_name="Ana",
         last_name= "MAria",
         email="email@gmail.com",
         role= [Role.role_1]
    ),
    User(id=UUID("9b4eca59-6129-42c7-af74-e4ac2ba30e66"),
         first_name="Otilia",
         last_name= "Santos",
         email="email@gmail.com",
         role= [Role.role_2]
    ),
    User(id=UUID("548704f5-2c0f-4679-96d7-7898c4cb1ca7"),
         first_name="Camila",
         last_name= "SIlva",
         email="email@gmail.com",
         role= [Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Olá, Womakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuario não encontrado!"}

@app.post("/api/users")
async def get_users(user: User):
    """
    Adicionar um usuario na base de dados
    
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_users(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail= f"Usuário com o id {id} não encontrado!"
    )