from pydantic import BaseModel, Field

class User(BaseModel):
    dni: str = Field(min_length=8, max_length=9, description='DNI del usuario')
    username: str = Field(min_length=6, max_length=25, description='Nombre de usuario')
    email: str = Field(min_length=6, max_length=50, description='correo electronico')
    password: str = Field(min_length=8, max_length=50, description='Contraseña del usuario')

    class config:
        from_attributes = True