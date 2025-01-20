from pydantic import BaseModel, EmailStr, datetime, Field
import uuid


class UserBase():
    user_id: str = Field(default=str(uuid.uuid4()), strip_whitespace=True, description="Unique identifier for the user.") 
    name: str = Field(strip_whitespace=True, description="Name of the user.") 
    email: EmailStr = Field(strip_whitespace=True, description="") 
    password: str = Field(strip_whitespace=True, description="")
    phone_number: str = Field(strip_whitespace=True, description="")
    attributes: dict = Field(strip_whitespace=True, description="")
    created_at: datetime = Field(strip_whitespace=True, description="")
    updated_at: datetime = Field(strip_whitespace=True, description="")



class UserCreate():
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str