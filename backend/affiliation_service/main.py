from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from database import SessionLocal, engine
from client.user_client import get_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/", response_model=schemas.Affiliation)
async def create_affiliation(affiliation: schemas.AffiliationCreate, db: Session = Depends(get_db)):
    # Verificar que el usuario existe
    user = await get_user(affiliation.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    
    return crud.create_affiliation(db=db, affiliation=affiliation)

@app.get("/{affiliation_id}", response_model=schemas.Affiliation)
async def read_affiliation(affiliation_id: int, db: Session = Depends(get_db)):
    db_affiliation = crud.get_affiliation(db, affiliation_id=affiliation_id)
    if db_affiliation is None:
        raise HTTPException(status_code=404, detail="Affiliation not found")
    
    # Obtener datos del usuario
    user_data = await get_user(db_affiliation.user_id)
    
    return {
        **db_affiliation.__dict__,
        "user": user_data
    }