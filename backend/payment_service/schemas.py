from enum import Enum
from pydantic import BaseModel, Field
from datetime import date

class PeriodEnum(str, Enum):
    ene = 'ene'
    feb = 'feb'
    mar = 'mar'
    abr = 'abr'
    may = 'may'
    jun = 'jun'
    jul = 'jul'
    ago = 'ago'
    sep = 'sep'
    oct = 'oct'
    nov = 'nov'
    dic = 'dic'

PERIOD_DB_MAP = {
    'ene' : 'ene',
    'feb' : 'feb',
    'mar' : 'mar',
    'abr' : 'abr',
    'may' : 'may',
    'jun' : 'jun',
    'jul' : 'jul',
    'ago' : 'ago',
    'sep' : 'sep',
    'oct' : 'oct',
    'nov' : 'nov',
    'dic' : 'dic',
}

class StatusEnum(int, Enum):
    a = 1
    i = 0

STATUS_DB_MAP = {
    'a' : 1,
    'i' : 0,
}

class Payment_schema(BaseModel):
    dni: str = Field(description='DNI del usuario')
    period: PeriodEnum = Field(description='Periodo de pago')
    amount: float = Field(description='monto del pago')
    payment_date: date = Field(description='Fecha de pago')
    status: int = Field(decription='estado de cobertura')

    class Config:
        from_attributes = True