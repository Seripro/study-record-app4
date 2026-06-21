from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import record
from app.schemas.record import RecordCreate

class RecordRepository:
    def get_records(db: Session):
        records = db.query(record.Record).all()
        return records

    def add_record(
        data: RecordCreate, 
        db: Session, 
    ):    
        # 新しいレコードを作成して保存
        new_record = record.Record(title=data.title, time=data.time)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record