from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import os

# from app.database import engine, get_db
# from app import models

# # サーバー起動時にテーブルを作成
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBearer(auto_error=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def get_hello():
    return "hello"

# @app.get("/hello")
# def get_hello(db: Session = Depends(get_db)):
#     favs = db.query(models.Favorite).all()
#     return favs
