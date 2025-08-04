from sqlalchemy import Column, String, Date, Boolean
from database import Base

class Authorization_model(Base):
    __tablename__ = 'authorization'
    dni = Column(String, primary_key=True, unique=True, index=True)
    request_date = Column(Date)
    authorization_status = Column(Boolean)
    justification = Column(String)