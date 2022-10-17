from pydantic import BaseModel
from typing import Optional,List, Union

class EmplySkill(BaseModel):
    id:int
    level:int

class Employee(BaseModel):
    id: Optional[str]
    name: str
    position: str
    skills: List[EmplySkill]
    
class EmployeeNoSkills(BaseModel):
    id: Optional[str]
    name: str
    position: str
