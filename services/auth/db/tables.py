from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class RestoClient(Base):
    __tablename__ = "clients"

    id = Column(Integer(), primary_key=True, unique=True,autoincrement=True)
    restoId = Column(Integer(), nullable=False) #send restoId as 0 while signing up the user
    first_name = Column(String(20),nullable=False)
    last_name = Column(String(20),nullable=True)
    email = Column(String(20), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    password = Column(String(100),unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)