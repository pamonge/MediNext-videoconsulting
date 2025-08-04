from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import Plan_schema
import models
from database import engine, SessionLocal

app = FastAPI(
    title='Plan Service'
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Retornar un plan 
@app.get('/plan', tags=['plan'])
async def get_all_plans(db: db_dependency):
    plans = db.query(models.Plan_model).all()
    if not plans:
        raise HTTPException(status_code=404, detail='No existen planes registrados')
    return plans

# Retornar un plan segun id
@app.get('/plan/{id}', tags=['plan'])
async def get_plan(id: int, db: db_dependency):
    plan = db.query(models.Plan_model).filter(models.Plan_model.id == id).first()
    if not plan:
        raise HTTPException(status_code=404, detail='plan no encontrado o inexistente')
    return plan

# Creat un plan
@app.post('/plan', tags=['plan'], response_model=Plan_schema)
async def post_plan(plan: Plan_schema, db: db_dependency):
    try:
        db_plan = models.Plan_model(**plan.dict())
        db.add(db_plan)
        db.commit()
        db.refresh(db_plan)
        return bd_plan
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'No se pudo crear el plan especificado: {str(e)}')

# Editar un plan
@app.put('plan/{id}', tags=['plan'], response_model=Plan_schema)
async def put_plan(id: int, plan: Plan_schema, db: db_dependency):
    plan_db = db.query(models.Plan_model).filter(models.Plan_model.id == id).first()
    if not plan_db:
        raise HTTPException(status_code=404, detail='Plan no encontrado o inexistente')
    try:
        plan_db.detail = plan.detail
        plan_db.name = plan.name
        db.commit()
        db.refresh(plan_db)
        return plan_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error al intentar actualizar el plan indicado: {str(e)}')

# Eliminar un plan
@app.delete('plan/{id}', tags=['plan'])
async def delete_plan(id: int, db: db_dependency):
    plan_db = db.query(models.Plan_model).filter(models.Plan_model.id)
    if not plan_db:
        raise HTTPException(status_code='500', detail='No se pudo eliminar en plan solicitado')
    try:
        db.delete(plan_db)
        db.commit()
        return {f'El plan {plan_db.id} a sido eliminado'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail='Error al intentar eliminar el plan seleccionado')