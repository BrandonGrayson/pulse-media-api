from sqlite3 import Timestamp
from sqlalchemy import Column, Integer, String, TIMESTAMP
from .database import Base
from sqlalchemy.sql.expression import text

class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))