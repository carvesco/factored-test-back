from fastapi import APIRouter, Response, status
from config.db import connection
from models.skill import skills
from schemas.skill import Skill
from starlette.status import HTTP_204_NO_CONTENT

skill = APIRouter()


@skill.get("/skills",response_model=list[Skill],tags=["skills"])
def get_skills():
    return connection.execute(skills.select()).fetchall()

@skill.post("/skills",response_model=Skill,tags=["skills"])
def create_skill(skill: Skill):
    new_skill = {"name": skill.name}
    result = connection.execute(skills.insert().values(new_skill))
    return connection.execute(skills.select().where(skills.c.id == result.lastrowid)).first()

@skill.delete("/skills/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["skills"])
def delete_user(id: str):
    connection.execute(skills.delete().where(skills.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
