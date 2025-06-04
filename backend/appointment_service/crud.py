from sqlalchemy.orm import Session
from models import Appointment
from schemas import AppointmentCreate
from sqlalchemy import and_

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appointment: AppointmentCreate):
    # Validar que no haya solapamiento de turnos del médico
    existing = db.query(Appointment).filter(
        and_(
            Appointment.doctor_username == appointment.doctor_username,
            Appointment.date_time == appointment.date_time
        )
    ).first()
    if existing:
        return None  # conflicto de horario
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment