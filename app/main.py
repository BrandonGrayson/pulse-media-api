from email.policy import default
import json
from fastapi import FastAPI, Header, Response, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .schemas import User, Service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = [
    'http://localhost:3000'
]

# The next Goal is to setup a database and put the user request in the db

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/service", status_code=status.HTTP_201_CREATED)
async def add_service(user: User, service: Service, db: Session = Depends(get_db)):
    print(user)
    print(service)
    # db_service = models.User(**user.dict())
    # db.add(db_service)
    # db.commit()
    # db.refresh()
    return Response(status_code=status.HTTP_201_CREATED)