from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.record import RecordService
from app.schemas.record import RecordCreate

router = APIRouter()

@router.get("/records")
def get_records(db: Session = Depends(get_db)):
    records = RecordService.get_records(db)
    return records

@router.post("/records", status_code=status.HTTP_201_CREATED)
def add_record(
    data: RecordCreate, 
    db: Session = Depends(get_db), 
):    
    
    # 新しいレコードを作成して保存
    message = RecordService.add_record(data, db)
    
    return message