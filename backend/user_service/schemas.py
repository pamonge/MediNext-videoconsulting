from pydantic import BaseModel, Field
import profile_schema, user_schema

# Uso de wraper para convinar los dos schemas
class User_Profile_Wraper(BaseModel):
    user: user_schema.User
    profile: profile_schema.Profile

    class Config:
        from_attributes = True