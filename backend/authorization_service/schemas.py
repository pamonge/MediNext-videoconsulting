from datetime import date
from pydantic import BaseModel, Field

class Authorization_schema(BaseModel):
    dni: str = Field(min_length=8, max_length=9, description='DNI del solicitante')
    request_date: date = Field(description='Fecha de solicitud, YYYY-MM-DD')
    authorization_status: bool = Field(default=False, description='Estado de la autorizacion')
    justification: str = Field(description='Justificación del pedido')

    class Config:
        from_attributes = True