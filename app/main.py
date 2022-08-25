from email.policy import default
import json
from fastapi import FastAPI, Header, Response, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

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

class Service(BaseModel):
    firstName: str
    lastName: str
    email: str
    services: List[str]

@app.post("/service", status_code=status.HTTP_201_CREATED)
async def add_service(service: Service):
    try:
        print((service))
    except ValueError as error:
        print(error)
    # print(type(service))
    return Response(status_code=status.HTTP_201_CREATED)