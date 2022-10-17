from pydantic import BaseModel
from typing import Optional

class Skill(BaseModel):
    id: Optional[str]
    name: str
