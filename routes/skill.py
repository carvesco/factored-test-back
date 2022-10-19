from fastapi import APIRouter, Response, status
from config.db import connection
from models.skill import skills
from schemas.skill import SkillSchema
from starlette.status import HTTP_204_NO_CONTENT

skill = APIRouter()


@skill.get("/skills",response_model=list[SkillSchema],tags=["skills"])
def get_skills():
    return connection.execute(skills.select()).fetchall()

@skill.post("/skills",response_model=SkillSchema,tags=["skills"])
def create_skill(skill: SkillSchema):
    new_skill = {"skillname": skill.skillname}
    result = connection.execute(skills.insert().values(new_skill))
    return connection.execute(skills.select().where(skills.c.id == result.lastrowid)).first()

@skill.delete("/skills/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["skills"])
def delete_skill(id: str):
    connection.execute(skills.delete().where(skills.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
