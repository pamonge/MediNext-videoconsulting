from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import Affiliation
import models
from database import engine, SessionLocal

app = FastAPI(
    title='Affiliation Service'
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

#Retorna una afiliacion según el numero de DNI
@app.get('/affiliation/{id}', tags=['Affiliation'])
async def get_affiliation(id: str, db: db_dependency):
    affiliation = db.query(models.Affiliation).filter(models.Affiliation.dni == id).first()
    if not affiliation:
        raise HTTPException(status_code=404, detail='No existe afiliado según el DNI proporcionado')
    return affiliation

# Retorna todas las afiliaciones
@app.get('/affiliation', tags=['Affiliation'])
async def get_all_affiliations(db: db_dependency):
    affiliations = db.query(models.Affiliation).all()
    if not affiliations:
        raise HTTPException(status_code=404, detail='No existen afiliados registrados')
    return affiliations

# Crear una afiliacion
@app.post('/affiliation', tags=['Affiliation'])
async def create_affiliation(affiliation: Affiliation, db: db_dependency):
    try:
        db_affiliation = models.Affiliation(**affiliation.dict())
        db.add(db_affiliation)
        db.commit()
        db.refresh(db_affiliation)
        return db_affiliation
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar crear un nuevo afiliado: {str(e)}')

# Actualizar una afiliacion
@app.put('/affiliation/{id}', tags=['Affiliation'])
async def update_affiliation(id: str, affiliation: Affiliation, db: db_dependency):
    db_affiliation = db.query(models.Affiliation).filter(models.Affiliation.dni == id).first()
    if not db_affiliation:
        raise HTTPException(status_code=404, detail='No existe afiliado según el DNI proporcionado')
    
    try:
        db_affiliation.active = affiliation.active
        db_affiliation.plan = affiliation.plan
        db.commit()
        db.refresh(db_affiliation)
        return db_affiliation
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar actualizar el registro: {str(e)}')

# Eliminar una afiliacion
@app.delete('/affiliation/{id}', tags=['Affiliation'])
async def delete_affiliation(id: str, db: db_dependency):
    db_affiliation = db.query(models.Affiliation).filter(models.Affiliation.dni == id).first()
    if not db_affiliation:
        raise HTTPException(status_code=404, detail='No existe afiliacion según el DNI proporcionado')
    try:
        db.delete(db_affiliation)
        db.commit()
        return {'detail' : 'Afiliacion eliminada correctamente'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al eliminar el registro especificado: {str(e)}')