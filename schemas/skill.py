from pydantic import BaseModel
from typing import Optional

class SkillSchema(BaseModel):
    id: Optional[str]
    skillname: str
