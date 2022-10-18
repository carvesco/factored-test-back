from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from yaml import load
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")


url = "mysql+pymysql://"+str(USER)+":"+str(PASSWORD) + \
    "@localhost:"+str(PORT)+"/"+str(DATABASE)
engine = create_engine(url,pool_recycle=3600, pool_size=25, max_overflow=5)

if not database_exists(engine.url):
    create_database(engine.url)

meta = MetaData()


connection = engine.connect()


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
seedSession = Session()
