from pydantic import BaseModel
from typing import Optional
from datetime import date
import enum

# Enums
class StatusEnum(str, enum.Enum):
    vigente = "v"
    sin_cobertura = "c"

class RelationshipEnum(str, enum.Enum):
    titular = "t"
    familiar = "f"

# Base común
class AffiliationBase(BaseModel):
    discharge_date: Optional[date] = None
    plan_id: Optional[int] = None
    status: StatusEnum
    relationship: RelationshipEnum

# Para crear una afiliación
class AffiliationCreate(AffiliationBase):
    beneficiary: int  # user_id obligatorio

# Para actualizar
class AffiliationUpdate(AffiliationBase):
    pass

# Para devolver desde la API
class AffiliationOut(AffiliationBase):
    affiliate_id: int
    beneficiary: int

    class Config:
        orm_mode = True