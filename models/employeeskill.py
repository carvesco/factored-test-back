from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
from sqlalchemy.orm import registry

mapper_registry = registry()

employeeskills = Table("employeeskills", meta, 
    Column("employeeId", Integer, ForeignKey("employees.id"), primary_key=True),
    Column("skillId", Integer, ForeignKey("skills.id"), primary_key=True),
    Column("skillLevel",Integer))

class Employeeskill(object):
    pass

mapper_registry.map_imperatively(Employeeskill, employeeskills)