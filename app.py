from fastapi import FastAPI
from routes.user import user
from routes.employee import employee
from routes.skill import skill
from routes.employeeskill import employeeskill
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import event
from models.employee import Employee,employees
from models.skill import Skill,skills
from models.employeeskill import Employeeskill,employeeskills
from config.db import seedSession,connection
import random as rand

# Crea un servidor basico

if (seedSession.query(Employee).first() == None):
    employ = {"name": "Cesar","lastname": "Velasco",
              "position": "Developer"}
    connection.execute(employees.insert().values(employ))
if (seedSession.query(Skill).first() == None):
    skillslist = [{"skillname": "Python"}, {"skillname": "Java"}, {"skillname": "C#"}, {"skillname": "JS"}, {
        "skillname": "SQL"}, {"skillname": "NoSql"}, {"skillname": "React"}, {"skillname": "Vue"}]
    connection.execute(skills.insert().values(skillslist))
if (seedSession.query(Employeeskill).first() == None):
    empskillslist = [{"employeeId": 1, "skillId": 1, "skillLevel": rand.randint(0, 10)}, {"employeeId": 1, "skillId": 2, "skillLevel": rand.randint(0, 10)}, {"employeeId": 1, "skillId": 3, "skillLevel": rand.randint(
        0, 10)}, {"employeeId": 1, "skillId": 4, "skillLevel": rand.randint(0, 10)}, {"employeeId": 1, "skillId": 6, "skillLevel": rand.randint(0, 10)}, {"employeeId": 1, "skillId": 8, "skillLevel": rand.randint(0, 10)}]
    connection.execute(employeeskills.insert().values(empskillslist))

seedSession.close()

app = FastAPI(
    title="factoredTestApi",
    description="backend for the factored technical test",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    },
        {
        "name": "employees",
        "description": "employees routes"

    }, {
        "name": "skills",
        "description": "skills routes"

    },
    ]
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user)
app.include_router(employee)
app.include_router(skill)
app.include_router(employeeskill)
