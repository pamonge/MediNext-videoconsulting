from sqlalchemy import Column, Integer, String, Date, BigInteger
from database import Base

class Profile(Base):
    __tablename__ = 'profile'
    dni = Column(String, unique=True, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    sex = Column(String, nullable=False) # 'm' o 'f'
    marital_status = Column(String, nullable=False) # 's', 'c', 'd', 'v'
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    role = Column(String, nullable=False) # 'a', 'u', 'm'
    image = Column(String, default='profilepics/defaultUser.png', nullable=True)  # Optional, guarda una imagen por defecto