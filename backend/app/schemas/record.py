from pydantic import BaseModel

class RecordCreate(BaseModel):
    title: str
    time: int
