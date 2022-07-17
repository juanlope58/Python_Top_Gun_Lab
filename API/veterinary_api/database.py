from sqlalchemy import Column, Integer, String, create_engine, true
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///veterinary.db")
base = declarative_base()


class Veterinary(base):
    __tablename__="mascota"
    id = Column(Integer, primary_key=true)
    name = Column(String(20))
    age = Column(Integer)
    race = Column(String(40))
    species = Column(String(40))
