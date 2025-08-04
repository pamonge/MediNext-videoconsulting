from sqlalchemy import Column, Float, String, Date, Integer
from database import Base

class Payment_model(Base):
    __tablename__ = 'payment'
    dni = Column(String, primary_key=True, unique=True, index=True)
    period = Column(String)
    amount = Column(Float)
    payment_date = Column(Date)
    status = Column(Integer)
