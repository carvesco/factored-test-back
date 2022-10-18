from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:password@localhost:3306/ftback")

meta = MetaData()

connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()