from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from .database import Base
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class Service(Base):
    __tablename__ = 'Services'

    id = Column(Integer, primary_key=True, nullable=False)
    google = Column(Boolean, nullable=True)
    web_development = Column(Boolean, nullable=True)
    social_media = Column(Boolean, nullable=True)