from sqlalchemy import Column, String
from database import Base

class User(Base):
    __tablename__ = 'user'
    dni = Column(String, unique=True, primary_key=True, index=True) #<<< seria la FK de la tabla profile
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)