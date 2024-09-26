from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base

engine = create_engine('sqlite:///my_db.db')
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)


def get_session():
    return Session()
