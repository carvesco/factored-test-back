from fastapi import FastAPI
from routes.user import user
# Crea un servidor basico
app = FastAPI(
    title="fastapi templt",
    description="fastapi basic api template",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)
app.include_router(user)
