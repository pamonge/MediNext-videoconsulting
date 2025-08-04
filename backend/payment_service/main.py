from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import Payment_schema
import models
from database import engine, SessionLocal

app = FastAPI(
    title='Payment Service',
)

models.Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]

# Obtener todos los pagos
@app.get('/payment', tags=['payment'])
async def get_all_payments(db: db_dependency):
    payments = db.query(models.Payment_model).all()
    if not payments:
        raise HTTPException(status_code=404, detail='No se encuentran pagos registrados')
    return payments

# Obtener un pago según id
@app.get('/payment/{id}', tags=['payment'])
async def get_payment_by_id(id: str, db: db_dependency):
    get_payment = db.query(models.Payment_model).filter(models.Payment_model.dni == id).first()
    if not get_payment:
        raise HTTPException(status_code=404, detail='Pago no encontrado o inexistente')
    return get_payment

# Crear nuevo registro de pago
@app.post('/payment', tags=['payment'])
async def post_payment(payment: Payment_schema, db: db_dependency):
    try:
        new_payment = models.Payment_model(**payment.dict())
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar crear el pago: {str(e)}')

# Actualizar pago 
@app.put('/payment/{id}', tags=['payment'])
async def update_payment(id: str, payment: Payment_schema, db: db_dependency):
    mod_payment = db.query(models.Payment_model).filter(models.Payment_model.dni == id).first()
    if not mod_payment:
        raise HTTPException(status_code=404, detail='Pago no encontrado o inexistente')
    try:
        mod_payment.period = payment.period
        mod_payment.amount = payment.amount
        mod_payment.payment_date = payment.payment_date
        mod_payment.status = payment.status
        db.commit()
        db.refresh(mod_payment)
        return mod_payment
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar actualizar el registro de pago: {str(e)}')

@app.delete('/payment/{id}', tags=['payment'])
async def delete_payment(id: str, db: db_dependency):
    del_payment = db.query(models.Payment_model).filter(models.Payment_model.dni == id).first()
    if not del_payment:
        raise HTTPException(status_code=404, detail='Pago no encontrado o inexistente')
    try: 
        db.delete(del_payment)
        db.commit()
        return {'detail': 'Registro eliminado correctamente'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar eliminar el registro: {str(e)}')

