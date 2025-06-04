from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    patient_username: str
    doctor_username: str
    date_time: datetime
    reason: str

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentOut(AppointmentBase):
    id: int

    class Config:
        orm_mode = True