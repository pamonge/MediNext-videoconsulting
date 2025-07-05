from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Crear un perfil básico vacío asociado al nuevo usuario
    try:
        response = httpx.post(
            "http://profile_service:8000/profile/",  #puede ser directamente o vía gateway
            json={"user_id": db_user.id}
        )
        response.raise_for_status()
    except httpx.RequestError as e:
        print(f"❌ Error al crear perfil: {e}")
    except httpx.HTTPStatusError as e:
        print(f"❌ Error HTTP al crear perfil: {e.response.status_code} - {e.response.text}")
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()