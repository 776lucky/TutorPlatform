# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    education_level: Optional[str] = None
    major: Optional[str] = None
    certifications: Optional[str] = None
    working_with_children_check: Optional[str] = None
    subjects: Optional[str] = None
    has_experience: Optional[bool] = None
    experience_details: Optional[str] = None
    availability: Optional[str] = None
    accepts_short_notice: Optional[bool] = None

# ✅ 创建 ProfileUpdate：全部字段都设置为可选
class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    education_level: Optional[str] = None
    major: Optional[str] = None
    certifications: Optional[str] = None
    working_with_children_check: Optional[str] = None
    subjects: Optional[str] = None
    has_experience: Optional[bool] = None
    experience_details: Optional[str] = None
    availability: Optional[str] = None
    accepts_short_notice: Optional[bool] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileOut(ProfileCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class UserCreate(ProfileBase):
    email: EmailStr
    password: str
    role: str = "student"

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
