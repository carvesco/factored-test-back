from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy_utils import database_exists, create_database


engine = create_engine("mysql+pymysql://root:password@localhost:3306/ftback",
                       pool_recycle=3600, pool_size=25, max_overflow=5)

if not database_exists(engine.url):
    create_database(engine.url)
    
meta = MetaData()


connection = engine.connect()



session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()


