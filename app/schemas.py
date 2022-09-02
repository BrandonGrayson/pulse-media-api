from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    firstName: str
    lastName: str
    email: str

class Service(BaseModel):
    google: Optional[bool]
    web_development: Optional[bool]
    social_media: Optional[bool]
