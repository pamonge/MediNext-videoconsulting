from datetime import date
from enum import Enum
from pydantic import BaseModel, Field

class PlanEnum(str, Enum):
    j = 'j' # jubilado
    m = 'm' # mediplus

PLAN_DB_MAP = {
    'j': 'jubilado',
    'm': 'mediplus',
}

class Affiliation(BaseModel):
    dni: str = Field(min_length=8, max_length=9, description='DNI del afiliado')
    discharge_date: date = Field(description='Fecha de alta del afiliado, YYYY-MM-DD')
    active: bool = Field(default=True, description='Estado de cobertura del afiliado')
    plan: PlanEnum = Field(description='Plan del afiliado', example='j o m')

    class Config:
        from_attributes = True