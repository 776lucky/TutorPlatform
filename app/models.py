from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Float

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    profile = relationship("Profile", back_populates="user", uselist=False)
    tasks = relationship("Task", back_populates="user")

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    education_level = Column(String(50), nullable=True)
    major = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    working_with_children_check = Column(String(50), nullable=True)
    subjects = Column(Text, nullable=True)
    has_experience = Column(Boolean, nullable=True)
    experience_details = Column(Text, nullable=True)
    availability = Column(Text, nullable=True)
    accepts_short_notice = Column(Boolean, nullable=True)
    lat = Column(Float, nullable=False, default=0.0)
    lng = Column(Float, nullable=False, default=0.0)
    hourly_rate = Column(Float, nullable=True)
    rating = Column(Float, nullable=True)
    title = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    user = relationship("User", back_populates="profile")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subject = Column(String)
    description = Column(String)
    address = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    budget = Column(String)
    deadline = Column(String)
    status = Column(String)
    posted_by = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))  # ✅ 添加这一行
    user = relationship("User", back_populates="tasks")  # ✅ 添加这一行


