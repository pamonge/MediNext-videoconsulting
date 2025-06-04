from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_username = Column(String, index=True)
    doctor_username = Column(String, index=True)
    date_time = Column(DateTime)
    reason = Column(String)