from sqlalchemy import Table, Column
import sqlalchemy
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine, session, connection
from models.employeeskill import employeeskills, Employeeskill
from sqlalchemy.orm import registry
import random as rand

mapper_registry = registry()

skills = Table("skills", meta,
               Column("id", Integer, primary_key=True),
               Column("skillname", String(255)))


class Skill(object):
    pass


mapper_registry.map_imperatively(Skill, skills)

skills.create(engine, checkfirst=True)
employeeskills.create(engine, checkfirst=True)


#if (session.query(Skill).first() == None):
#    skillslist = [{"skillname": "Python"}, {"skillname": "Java"}, {"skillname": "C#"}, {"skillname": "JS"}, {
#        "skillname": "SQL"}, {"skillname": "NoSql"}, {"skillname": "React"}, {"skillname": "Vue"}]
#    connection.execute(skills.insert().values(skillslist))



