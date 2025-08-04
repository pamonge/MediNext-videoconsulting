from sqlalchemy import Column, Integer, String
from database import Base

class Plan_model(Base):
    __tablename__ = 'plan'
    plan_id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    detail = Column(String)
    name = Column(String)