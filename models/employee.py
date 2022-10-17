from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

employees = Table("employees", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("position", String(255)))
    
employees.create(engine,checkfirst=True)