import datetime
from pydantic import BaseModel


class NoteBase(BaseModel):
    text: str


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class Note(NoteBase):
    id_n: int
    views: int
    date_created: datetime.datetime
    date_update: datetime.datetime

    class Config:
        orm_mode = True
