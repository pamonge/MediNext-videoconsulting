# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# import models, schemas, crud

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Affiliation Service",
#     description="Microservicio para gestionar afiliaciones",
#     version="1.0.0",
#     docs_url="/docs"
# )

# # Dependency para obtener la sesión de base de datos
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Crear afiliación
# @app.post("/affiliations/", response_model=schemas.AffiliationOut)
# def create_affiliation(aff: schemas.AffiliationCreate, db: Session = Depends(get_db)):
#     return crud.create_affiliation(db, aff)

# # Listar todas
# @app.get("/affiliations/", response_model=list[schemas.AffiliationOut])
# def list_affiliations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return crud.get_affiliations(db, skip=skip, limit=limit)

# # Buscar una por ID
# @app.get("/affiliations/{affiliate_id}", response_model=schemas.AffiliationOut)
# def get_affiliation(affiliate_id: int, db: Session = Depends(get_db)):
#     aff = crud.get_affiliation_by_id(db, affiliate_id)
#     if not aff:
#         raise HTTPException(status_code=404, detail="Afiliación no encontrada")
#     return aff

# # Actualizar
# @app.put("/affiliations/{affiliate_id}", response_model=schemas.AffiliationOut)
# def update_affiliation(affiliate_id: int, aff_data: schemas.AffiliationUpdate, db: Session = Depends(get_db)):
#     return crud.update_affiliation(db, affiliate_id, aff_data)

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ./ import models, schemas, crud
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

@app.post("/affiliations/", response_model=schemas.Affiliation)
async def create_affiliation(affiliation: schemas.AffiliationCreate, db: Session = Depends(get_db)):
    # Verificar que el usuario existe
    user = await get_user(affiliation.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    
    return crud.create_affiliation(db=db, affiliation=affiliation)

@app.get("/affiliations/{affiliation_id}", response_model=schemas.Affiliation)
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