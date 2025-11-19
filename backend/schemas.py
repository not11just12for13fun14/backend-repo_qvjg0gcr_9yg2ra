"""
Database Schemas for Real Estate Media Inquiries

Each Pydantic model represents a collection. Collection name is the lowercase
of the class name. Example: Inquiry -> "inquiry" collection
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
  name: str = Field(..., description="Client name")
  email: EmailStr = Field(..., description="Client email")
  service: str = Field(..., description="Service requested (Photos, 3D Matterport, Video, Drone, Twilight)")
  message: Optional[str] = Field(None, description="Additional details like address, date, sqft")
