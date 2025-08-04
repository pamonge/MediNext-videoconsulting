from enum import Enum
from pydantic import BaseModel, Field

class PlanEnum(str, Enum):
    j = 'j' # jubilado
    m = 'm' # mediplus

PLANSERVICE_DB_MAP = {
    'j' : 'jubilado',
    'm' : 'mediplus',
}

class Plan_schema(BaseModel):
    plan_id: int = Field(description='identificación del plan')
    detail: str = Field(description='Detalle del plan')
    name: str = Field(description='Nombre del plan')
    
    class Config:
        from_attributes = True