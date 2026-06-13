from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import os

from app.database import engine, get_db
from app import models

# サーバー起動時にテーブルを作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBearer(auto_error=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecordCreate(BaseModel):
    title: str
    time: int

@app.get("/hello")
def get_hello():
    return "hello"

@app.get("/records")
def get_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records

@app.post("/records", status_code=status.HTTP_201_CREATED)
def add_record(
    data: RecordCreate, 
    db: Session = Depends(get_db), 
):    
    
    # 新しいレコードを作成して保存
    new_record = models.Record(title=data.title, time=data.time)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    
    return {"message": "記録を追加しました", "data": new_record}