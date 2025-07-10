# from sqlalchemy.orm import Session
# from models import Affiliation
# from schemas import AffiliationCreate

# # Crear nueva afiliación
# def create_affiliation(db: Session, affiliation: AffiliationCreate):
#     db_affiliation = Affiliation(**affiliation.dict())
#     db.add(db_affiliation)
#     db.commit()
#     db.refresh(db_affiliation)
#     return db_affiliation

# # Obtener afiliación por ID de usuario
# def get_affiliation_by_user(db: Session, user_id: int):
#     return db.query(Affiliation).filter(Affiliation.beneficiary == user_id).first()

# # Listar todas las afiliaciones
# def get_affiliations(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Affiliation).offset(skip).limit(limit).all()

from sqlalchemy.orm import Session
from . import models, schemas

def create_affiliation(db: Session, affiliation: schemas.AffiliationCreate):
    db_affiliation = models.Affiliation(**affiliation.model_dump())
    db.add(db_affiliation)
    db.commit()
    db.refresh(db_affiliation)
    return db_affiliation

def get_affiliation(db: Session, affiliation_id: int):
    return db.query(models.Affiliation).filter(models.Affiliation.id == affiliation_id).first()