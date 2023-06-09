import datetime
from typing import List

from pydantic import BaseModel

from app_notes.schema import Note


class BoardBase(BaseModel):
    title: str


class BoardCreate(BoardBase):
    pass


class BoardUpdate(BoardBase):
    pass


class Board(BoardBase):
    id: int
    time_created: datetime.date
    notes: List[Note] = []

    class Config:
        orm_mode = True
