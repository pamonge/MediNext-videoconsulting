from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import Authorization_schema
import models
from database import SessionLocal, engine

app = FastAPI(
    title='authorization service'
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/authorization/{id}", tags=['authorization service'])
async def get_authorization(id: str, db: db_dependency):
    db_authorization = db.query(models.Authorization_model).filter(models.Authorization_model.dni == id).first()
    if not db_authorization:
        raise HTTPException(status_code=404, detail="Autorizacion no encontrada o inaxistente.")
    return db_authorization

@app.post("/authorization", tags=['authorization service'])
def create_authorization(new_authoriztion: Authorization_schema, db: db_dependency):
    try:
        db_authorization = models.Authorization_model(**new_authorization.dict())
        db.add(db_authorization)
        db.commit()
        db.refresh(db_authorization)
        return db_authorization
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar crear una nueva autorizacion: {str(e)}')

@app.put('/authorization/{id}', tags=['authorization service'])
async def put_authorization(id: str, mod_authorization: Authorization_schema, db: db_dependency):
    db_authorization = db.query(models.Authorization_model).filter(models.Authorization_model.dni == id).first()
    if not db_authorization:
        raise HTTPException(status_code=404, detail='Autorizacion no encontrada o inexistente')
    try:
        db_authorization.authorization_status = mod_authorization.authorization_status
        db_authorization.justification = mod_authorization.justification
        db.commit()
        db.refresh(db_authorization)
        return db_authorization
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'No se pudo realizar la actualizacion de la autorizacion: {str(e)}')

    @app.delete('authorization/{id}', tags=['authorization service'])
    async def delete_authorization(id: str, db: db_dependency):
        db_authorization: db.query(models.Authorization_model).filter(models.Authorization_model.dni == id).first()
        if not db_authorization:
            raise HTTPException(status_code=404, detail='Autorizacion no encontrada o inexistente')
        try:
            db.delete(db_authorization)
            db.commit()
            return{'detail': 'Autorizacion eliminada con éxito'}
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f'Error al intentar eliminar la autorización: {str(e)}')