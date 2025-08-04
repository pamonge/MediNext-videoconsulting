from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import Medical_History_Schema
import models
from database import engine, SessionLocal

app = FastAPI(
    title='Medical History Service'
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Retorna todas las historias médicas
@app.get('/med_hist', tags=['medical history'], response_model=List[Medical_History_Schema])
async def get_all_med_hist(db: db_dependency):
    all_med_hist = db.query(models.Medical_History).all()
    if not all_med_hist:
        raise HTTPException(status_code=404, detail='No hay historias médicas guardadas')
    return all_med_hist

# Retorna una historia médica affiliate_id
@app.get('/med_hist/{id}', tags=['medical history'], response_model=Medical_History_Schema)
async def get_med_his_by_id(id: str, db: db_dependency):
    get_med_hist = db.query(models.Medical_History).filter(models.Medical_History.affiliate_id == id).first()
    if not get_med_hist:
        raise HTTPException(status_code=404, detail='Historia medica no encontrada o inexistente')
    return get_med_hist

# Crea una historia clínica
@app.post('/med_hist', tags=['medical history'])
async def post_med_hist(medicalHistory: Medical_History_Schema, db: db_dependency):
    try:
        db_medical_history = models.Medical_History(**medicalHistory.dict())
        db.add(db_medical_history)
        db.commit()
        db.refresh(db_medical_history)
    except Exception as e:
        db.rollback()
        raise HTTPExcception(status_code=500, detail=f'Error al intentar crean una historia clinica: {str(e)}')

# Actualiza una historia clinica segun dni
@app.put('/med_hist/{id}', tags=['medical history'])
async def put_med_hist(id: str, update_med_hist: Medical_History_Schema, db: db_dependency):
    db_med_hist = db.query(models.Medical_history).filter(models.Medical_History.affiliate_dni).all()
    if not db_med_hist:
        raise HTTPException(status_code=404, detail='Historia médica no encontrada o inexistente')
    try:
        db_med_hist.affiliate_dni = update_med_hist.affiliate_dni
        db_med_hist.consultation_date = update_med_hist.consultation_date
        db_med_hist.professional = update_med_hist.professional
        db_med_hist.diagnostic = update_med_hist.diagnostic
        db.commit()
        db.refresh(db_med_hist)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'No se ha podido actualizar la historia médica: {str(e)}')

# Elimina una historia clinica según dni
@app.delete('/med_hist/{id}', tags=['medical history'])
async def delete_med_his(id: str, db: db_dependency):
    db_med_hist = db.query(models.Medical_History).filter(models.Medical_History).first()
    if not db_med_hist:
        raise HTTPException(status_code=404, detail='Historia medica no encontrada o inexistente')
    try:
        db.delete(db_med_hist)
        db.commit()
        return{'detail': 'Historia medica eliminada con éxito'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar eliminar la historia medica: {str(e)}')