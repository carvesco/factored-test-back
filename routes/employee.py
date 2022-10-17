from fastapi import APIRouter, Response, status
from config.db import connection
from models.employee import employees
from models.employeeskill import employeeskills
from schemas.employee import Employee, EmployeeNoSkills
from starlette.status import HTTP_204_NO_CONTENT

employee = APIRouter()


@employee.get("/employees",response_model=list[EmployeeNoSkills],tags=["employees"])
def get_employees():
    return connection.execute(employees.select()).fetchall()

@employee.post("/employees",response_model=EmployeeNoSkills,tags=["employees"])
def create_employee(employee: Employee):
    new_employee = {"name": employee.name,
                "position": employee.position}
    
    result = connection.execute(employees.insert().values(new_employee))
    emp = connection.execute(employees.select().where(employees.c.id == result.lastrowid)).first()
    if(emp != None):
        print(emp[0])
        employee_id = emp[0]
        for i in employee.skills:
            print(i)
            emp_skill = {"employeeId":employee_id,"skillId":i.id,"skillLevel":i.level}
            connection.execute(employeeskills.insert().values(emp_skill))
    return emp

@employee.delete("/employees/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["employees"])
def delete_employee(id: str):
    connection.execute(employees.delete().where(employees.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

