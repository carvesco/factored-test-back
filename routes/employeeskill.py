from fastapi import APIRouter, Response, status
from config.db import connection
from models.employeeskill import employeeskills
from schemas.employeeskill import EmployeeSkillSchema
from starlette.status import HTTP_204_NO_CONTENT

employeeskill = APIRouter()


@employeeskill.get("/employeeskills",response_model=list[EmployeeSkillSchema],tags=["employeeSkills"])
def get_employeeskills():
    return connection.execute(employeeskills.select()).fetchall()
