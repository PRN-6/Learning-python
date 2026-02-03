from fastapi import FastAPI, HttpException
from pydantic import BaseModel 
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI()

class User(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime

class UserCreate(BaseModel):
    username: str
    email: str


class post(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    created_at: datetime
    updated_at: datetime


@app.get("/")
def read_root():
    return {"hello world"}

def main():
    print("Hello from my-backend!")

    
if __name__ == "__main__":
    main()
