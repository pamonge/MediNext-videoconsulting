from pydantic import BaseModel, Field
import profile_schema, user_schema

# Uso de wrapper para convinar los dos schemas
class User_Profile_Wrapper(BaseModel):
    user: user_schema.User
    profile: profile_schema.Profile

    class Config:
        from_attributes = True

# Token JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Datos extraidos del Token
class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None