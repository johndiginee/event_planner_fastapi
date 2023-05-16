from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": fastapi@john.com,
                "username": "admin12345"
                "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": fastapi@john.com,
                "password": "admin12345",
                "events": [],
            }
        }