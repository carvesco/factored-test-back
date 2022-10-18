from pydantic import BaseModel
from typing import Optional

class EmployeeSkillSchema(BaseModel):
    employeeId: int
    skillId: int
    skillLevel: int
