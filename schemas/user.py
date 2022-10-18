from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str
