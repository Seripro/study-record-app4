from sqlalchemy.orm import Session

from app.repositories.record import RecordRepository
from app.schemas.record import RecordCreate

class RecordService:
    def get_records(db: Session):
        records = RecordRepository.get_records(db)
        return records

    def add_record(
        data: RecordCreate, 
        db: Session, 
    ):    
        new_record = RecordRepository.add_record(data, db)
        
        return {"message": "記録を追加しました", "data": new_record}