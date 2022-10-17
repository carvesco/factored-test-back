from fastapi import FastAPI
from routes.user import user
from routes.employee import employee
from routes.skill import skill
from routes.employeeskill import employeeskill
# Crea un servidor basico
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

    }]
)
app.include_router(user)
app.include_router(employee)
app.include_router(skill)
app.include_router(employeeskill)
