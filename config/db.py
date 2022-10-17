from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:password@localhost:3306/factoredtestback")

meta = MetaData()

connection = engine.connect()
