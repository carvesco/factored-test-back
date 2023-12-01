from typing import List

from fastapi import APIRouter, Response, status
from config.db import connection
from models.user import users
from schemas.user import UserSchema
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()


@user.get("/users",response_model=List[UserSchema],tags=["users"])
def get_users():
    return connection.execute(users.select()).fetchall()


@user.post("/users",response_model=UserSchema,tags=["users"])
def create_user(user: UserSchema):
    new_user = {"name": user.name,
                "email": user.email, "password": user.password}
    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}",response_model=UserSchema,tags=["users"])
def get_user(id: str):
    return connection.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["users"])
def delete_user(id: str):
    connection.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}",response_model=UserSchema,tags=["users"])
def update_user(id: str, user: UserSchema):
    connection.execute(users.update(
        name=user.name, email=user.email, password=user.password).where(users.c.id == id))
    return connection.execute(users.select().where(users.c.id == id)).first()
