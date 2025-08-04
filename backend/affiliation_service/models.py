from sqlalchemy import Column, String, Date, Boolean
from database import Base

class Affiliation(Base):
    __tablename__ = 'affiliation'
    dni = Column(String, primary_key=True, unique=True, index=True)
    discharge_date = Column(Date)
    active = Column(Boolean)
    plan = Column(String)