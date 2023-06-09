from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event
from beanie import Document, Link

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@john.com",
                "password": "admin12345",
                "username": "admin"
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@john.com",
                "password": "admin12345",
            }
        }