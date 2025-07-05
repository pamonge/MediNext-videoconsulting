from pydantic import BaseModel
from typing import Optional
from datetime import date
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
    administrativo = "a"
    medico = "m"
    afiliado = "s"

class ProfileBase(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    birthdate: Optional[date] = None
    sex: Optional[SexEnum] = None
    marital_status: Optional[MaritalStatusEnum] = None
    address: Optional[str] = None
    phone: Optional[int] = None
    role: Optional[RoleEnum] = None
    profileImg: Optional[str] = None

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileUpdate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    dni: int
    user_id: int

    class Config:
        orm_mode = True