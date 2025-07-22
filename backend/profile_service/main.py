from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from typing import List, Annotated
from schemas import Profile
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(
    title = 'Profile Service'
)
app.mount('/profilepics', StaticFiles(directory='profilepics'))

#Crea todas las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Retorna un perfil según el id proporcionado
@app.get('/profile/{id}', tags=['Profile'], response_model=Profile)
async def get_profile(id: str, db: db_dependency):
    profile = db.query(models.Profile).filter(models.Profile.dni == id).first()
    if not profile:
        raise HTTPException(status_code=404, detail='Perfil no encontrado o inexistente')
    return profile

# Retorna todos los perfiles
@app.get('/profile', tags=['Profile'], response_model=List[Profile])
async def get_all_profiles(db: db_dependency):
    profiles = db.query(models.Profile).all()
    if not profiles:
        raise HTTPException(status_code=404, detail='No hay perfiles registrados')
    return profiles

# Crea un perfil nuevo
@app.post('/profile', tags=['Profile'])
async def create_profile(profile: Profile, db: db_dependency):
    try:
        # Verifica si el DNI ya existe
        existing_profile = db.query(models.Profile).filter(models.Profile.dni == profile.dni).first()
        if existing_profile:
            raise HTTPException(status_code=400, detail='DNI ya existe')
        db_profile = models.Profile(
            dni = profile.dni,
            name = profile.name,
            last_name = profile.last_name,
            birthdate = profile.birthdate,
            sex = profile.sex,
            marital_status = profile.marital_status,
            address = profile.address,
            phone = profile.phone,
            role = profile.role,
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile
    except Exception as e:
        raise HTTPException (status_code=404, detail=f'Error al crear el perfil: {str(e)}')

# Actualiza un perfil existente
@app.put('/profile/{id}', response_model=Profile, tags=['Profile'])
async def update_profile(id: str, profile: Profile, db: db_dependency):
    db_profile = db.query(models.Profile).filter(models.Profile.dni == id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail='Perfil no encontrado o inexistente') 
    try:
        db_profile.name = profile.name
        db_profile.last_name = profile.last_name
        db_profile.birthdate = profile.birthdate
        db_profile.sex = profile.sex
        db_profile.marital_status = profile.marital_status
        db_profile.address = profile.address
        db_profile.phone = profile.phone
        db_profile.role = profile.role
        db.commit()
        db.refresh(db_profile)
        return db_profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=f'Error al actualizar el perfil: {str(e)}')

# Actualiza la imagen de un perfil existente
@app.put('/profile/{id}/image', tags=['Profile'])
async def update_profile_image(id: str, image: str, db: db_dependency):
    db_profile = db.query(models.Profile).filter(models.Profile.dni == id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail='Perfil no encontrado o inexistente')
    try:
        db_profile.image = image
        db.commit()
        db.refresh(db_profile)
        return db_profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=f'Error al intentar actualizar la imagen de perfil: {str(e)}')

# Eliminar un perfil
@app.delete('/profile/{id}', tags=['Profile'])
async def delete_profile(id: str, db: db_dependency):
    db_profile = db.query(models.Profile).filter(models.Profile.dni == id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail='Perfil no encontrado o inexistente')
        try:
            db.delete(db_profile)
            db.commit()
            db.refresh(db_profile)
            return(f'Perfil con DNI {id} eliminado exitosamente')
        except Exception as e:
            raise HTTPException(status_code=404, detail=f'Error al eliminar perfil: {str(e)}')