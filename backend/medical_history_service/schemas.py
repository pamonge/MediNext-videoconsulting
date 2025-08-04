from datetime import date
from pydantic import BaseModel, Field

class Medical_History_Schema(BaseModel):
    history_id: int = Field(description='Id de la historia clinica')
    affiliate_dni: str = Field(description='DNI del afiliado')
    consultation_date: date = Field(description='Fecha de la consulta, YYYY-MM-DD')
    professional: str = Field(description='DNI de profesional que realizó la consulta')
    diagnostic: str = Field(description='Diagnostico del paciente')

    class Config:
        from_attributes = True