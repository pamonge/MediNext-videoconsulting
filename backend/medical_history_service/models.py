from sqlalchemy import Column, String, Date, Integer
from database import Base

class Medical_History(Base):
    __tablename__ = 'medical_history'
    history_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    affiliate_dni = Column(String)
    consultation_date = Column(Date)
    professional = Column(String)
    diagnostic = Column(String)

