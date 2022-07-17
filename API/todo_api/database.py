from sqlalchemy import Column, Integer, String, create_engine, true
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///todooo.db")
#create declarative database instance
Base = declarative_base()

#create todo table
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=true)
    task = Column(String(100))
