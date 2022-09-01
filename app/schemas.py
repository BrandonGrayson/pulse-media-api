from pydantic import BaseModel

class User(BaseModel):
    firstName: str
    lastName: str
    email: str

class Service(BaseModel):
    google: bool
    web_development: bool
    social_media: bool
