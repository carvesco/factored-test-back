from pydantic import BaseModel
from typing import Optional,List, Union

class EmplySkill(BaseModel):
    id:int
    level:int

class EmployeeSchema(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    position: str
    skills: List[EmplySkill]
    
class EmployeeNoSkillsSchema(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    position: str
