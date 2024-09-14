from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings,Settings

setting = get_settings()

SQLALCHEMY_DATABASE_URL = "mysql://admin:"+ setting.db_key +"@host.docker.internal:3306/rpgEncounter"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()