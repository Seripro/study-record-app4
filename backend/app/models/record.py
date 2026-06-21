from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from ..database import Base

class Record(Base):
    __tablename__ = "study-record"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    time = Column(Integer, index=True)
