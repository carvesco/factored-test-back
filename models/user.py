from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine
from sqlalchemy.orm import registry

mapper_registry = registry()

users = Table("users", meta, Column(
    "id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)), 
    Column("password", String(255)))
    
class User(object):
    pass

mapper_registry.map_imperatively(User, users)

users.create(engine,checkfirst=True)