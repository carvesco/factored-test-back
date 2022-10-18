from fastapi import APIRouter, Response, status
from config.db import connection, session
from models.employee import employees, Employee
from models.employeeskill import employeeskills, Employeeskill
from models.skill import Skill, skills
from schemas.employee import EmployeeSchema, EmployeeNoSkillsSchema
from schemas.employeeskill import EmployeeSkillSchema
from starlette.status import HTTP_204_NO_CONTENT

employee = APIRouter()


@employee.get("/employees", response_model=list[EmployeeNoSkillsSchema], tags=["employees"])
def get_employees():
    return connection.execute(employees.select()).fetchall()


@employee.post("/employees", response_model=EmployeeNoSkillsSchema, tags=["employees"])
def create_employee(employee: EmployeeSchema):
    new_employee = {"name": employee.name,
                    "position": employee.position}

    result = connection.execute(employees.insert().values(new_employee))
    emp = connection.execute(employees.select().where(
        employees.c.id == result.lastrowid)).first()
    if (emp != None):
        print(emp[0])
        employee_id = emp[0]
        for i in employee.skills:
            print(i)
            emp_skill = {"employeeId": employee_id,
                         "skillId": i.id, "skillLevel": i.level}
            connection.execute(employeeskills.insert().values(emp_skill))
    return emp


@employee.delete("/employees/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["employees"])
def delete_employee(id: str):
    connection.execute(employees.delete().where(employees.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@employee.get("/employees/{id}", tags=["employees"])
def get_employee_skills(id: str):
    query = session.query(Employee, Employeeskill, Skill).filter(
        employees.c.id == employeeskills.c.employeeId).filter(employeeskills.c.skillId == skills.c.id).with_entities(employees, employeeskills, skills).where(employees.c.id == id)
    return query.all()
