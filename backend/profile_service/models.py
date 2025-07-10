from sqlalchemy import Column, Integer, String, BigInteger, Date, Enum, ForeignKey
from database import Base
import enum

class SexEnum(str, enum.Enum):
    hombre = "h"
    mujer = "m"

class MaritalStatusEnum(str, enum.Enum):
    casado = "c"
    soltero = "s"
    viudo = "v"
    divorciado = "d"

class RoleEnum(str, enum.Enum):
    administrativo : "a"
    medico : "m"
    afiliado : "s"

class Profile(Base):
    __tablename__ = "profile"

    dni = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(Integer, models.ForeignKey("user.id", on_delete=models.CASCADE))
    name = Column(String, nullable = True)
    last_name = Column(String, nullable = True)
    birthdate = Column(Date, nullable = True)
    sex = Column(Enum(SexEnum), nullable = True)
    marital_status = Column(Enum(MaritalStatusEnum), nullable = True)
    address = Column(String, nullable = True)
    phone = Column(BigInteger, nullable = True)
    role = Column(Enum(RoleEnum), nullable = True)
    profileImg = Column(String) 

    user = relationship("user", back_populates = "profile")
