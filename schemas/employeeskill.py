from pydantic import BaseModel
from typing import Optional

class EmployeeSkill(BaseModel):
    employeeId: int
    skillId: int
    skillLevel: int
