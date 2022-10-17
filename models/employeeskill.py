from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

employeeskills = Table("employeeskills", meta, 
    Column("employeeId", Integer, ForeignKey("employees.id")),
    Column("skillId", Integer, ForeignKey("skills.id")),
    Column("skillLevel",Integer))
