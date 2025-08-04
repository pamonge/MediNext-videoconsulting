from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from schemas import User_Profile_Wraper
from user_schema import User
import models
from database import engine, SessionLocal
import httpx

app = FastAPI(
    title='User Service',
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Retorna todos los usuarios
@app.get('/get_all', tags=['User'], response_model=List[User])
async def get_all_users(db: db_dependency):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail='No hay usuarios registrados')
        users = {'detail': 'Usuario no registrado en user_service'}
    return users

#retorna un usuario por id
@app.get('/get_by/{id}', tags=['User'], response_model=User)
async def get_user_by_id(id: str, db: db_dependency):
    user = db.query(models.User).filter(models.User.dni == id).first()
    if not user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado o inexistente')
        user = {'detail': 'Usuario no registrado en user_service'}
    return user

# Crear un nuevo usuario
@app.post('/post', tags=['User'], response_model=User)
async def post_user(request: User_Profile_Wraper, db: db_dependency):
    user_data = request.user
    profile_data = request.profile

    # Verificar si el usuario ya existe
    existing_user = db.query(models.User).filter(models.User.dni == user_data.dni).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='El usuario ya existe')
    
    try:
        new_user = models.User(**user_data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        # Creacion de un nuevo perfil de manera automática al crear un nuevo usuario
        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    'http://profile_service:8000/profile', 
                    json=profile_data.dict()
                )
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f'No se pudo crear el perfil del usuario: {str(e)}')

        return new_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'No pudo crearse el usuario especificado: {str(e)}')

# Actualizar un usuario
@app.put('/put_by/{id}', tags=['User'], response_model=User)
async def update_user(id: str, user: User, db: db_dependency):
    update_user = db.query(models.User).filter(models.User.dni == id).first()
    if not update_user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado o inexistente')
    try:
        update_user.email = user.email
        update_user.password = user.password
        db.commit()
        db.refresh(update_user)
        return update_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al actualizar el usuario: {str(e)}')

# Eliminar usuario
@app.delete('/del/{id}', tags=['User'])
async def delete_user(id: str, db: db_dependency):
    user_delete = db.query(models.User).filter(models.User.dni == id).first()
    if not user_delete:
        raise HTTPException(status_code=404, detail='Usuario no encontrado o inexistente')
    try:
        db.delete(user_delete)
        db.commit()
        return {f'Usuario eliminado: {user_delete.dni}'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error al intentar eliminar el usuario: {str(e)}')