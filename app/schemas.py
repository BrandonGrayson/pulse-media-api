from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    firstName: str
    lastName: str
    email: str

class Service(BaseModel):
    google: Optional[bool] = False
    web_development: Optional[bool] = False
    social_media: Optional[bool] = False
