from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine
from sqlalchemy.orm import registry

mapper_registry = registry()

employees = Table("employees", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("position", String(255)))
    
    
class Employee(object):
    pass

mapper_registry.map_imperatively(Employee, employees)


employees.create(engine,checkfirst=True)