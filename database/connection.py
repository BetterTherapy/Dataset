from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .model import Base
from config import config


engine = create_engine(config.database_url, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db():
    Base.metadata.create_all(bind=engine)
