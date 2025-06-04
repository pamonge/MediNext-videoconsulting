from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/appointments/", response_model=schemas.AppointmentOut)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    result = crud.create_appointment(db, appointment)
    if result is None:
        raise HTTPException(status_code=409, detail="Turno ya ocupado por el médico")
    return result

@app.get("/appointments/", response_model=list[schemas.AppointmentOut])
def list_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_appointments(db, skip=skip, limit=limit)