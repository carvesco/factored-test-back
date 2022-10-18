from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine
from models.employeeskill import employeeskills
from sqlalchemy.orm import registry

mapper_registry = registry()

skills = Table("skills", meta, 
    Column("id", Integer, primary_key=True),
    Column("skillname", String(255)))
    
class Skill(object):
    pass

mapper_registry.map_imperatively(Skill, skills)    
    
skills.create(engine,checkfirst=True)
employeeskills.create(engine,checkfirst=True)