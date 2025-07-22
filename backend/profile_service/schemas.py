from datetime import date
from enum import Enum
from pydantic import BaseModel, Field

class GenderEnum(str, Enum):
    m = 'm' #masculino
    f = 'f' #femenino

GENDER_DB_MAP = {   
    'm': 'masculino',
    'f': 'femenino',
}

class Marital_StatusEnum(str, Enum):
    s = 's' #soltero
    c = 'c' #casado
    d = 'd' #divorciado
    v = 'v' #viudo

MARITAL_STATUS_DB_MAP = {
    's': 'soltero',
    'c': 'casado',
    'd': 'divorciado',  
    'v': 'viudo',
}

class RoleEnum(str, Enum):
    a = 'a' #admin
    u = 'u' #usuario
    m = 'm' #medico

ROLAE_DB_MAP = {
    'a': 'admin',
    'u': 'usuario',
    'm': 'medico',
}

class Profile(BaseModel):
    dni : str = Field(min_length=8, max_length=9, description='DNI del usuario')
    name : str = Field(min_length=3, max_length=35, description='Nombre mayor a tres letras')
    last_name : str = Field(min_length=3, max_length=50, description='Apellido superior a 3 letras')
    birthdate: date = Field(gt='1900-01-01', description='Fecha de nacimiento con formato YYYY-MM-DD')
    sex: GenderEnum = Field(description='Sexo biologico del usuario', example= 'm o f')
    marital_status: Marital_StatusEnum = Field(description= 'Estado civil', example='s, c, d o v')
    address: str = Field(min_length=3, max_length=50, description='Direccion')
    phone: str = Field(min_length=9, max_length=11, description='Numero de contacto')
    role: RoleEnum = Field(description='Rol del usuario', example='a, u o m')
    image: str = Field(default=None, description='URL de la imagen de perfil')

    class Config:        # Permite que FastAPI convierta automáticamente modelos de SQLAlchemy en respuestas compatibles con Pydantic.
        orm_mode = True