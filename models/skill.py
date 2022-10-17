from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine
from models.employeeskill import employeeskills

skills = Table("skills", meta, 
    Column("id", Integer, primary_key=True),
    Column("name", String(255)))
    
skills.create(engine,checkfirst=True)
employeeskills.create(engine,checkfirst=True)