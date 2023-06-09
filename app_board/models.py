import sqlalchemy
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, func

from database import metadata


boards = sqlalchemy.Table(
    "boards",
    metadata,
    sqlalchemy.Column("id_b", Integer, primary_key=True),
    sqlalchemy.Column("date_created", DateTime, default=func.now()),
    sqlalchemy.Column("date_update", DateTime, default=func.now(), onupdate=func.now()),
    sqlalchemy.Column("title", String()),
)


note_on_board = sqlalchemy.Table(
    "note_on_board",
    metadata,
    sqlalchemy.Column("id", ForeignKey("notes.id_n"), primary_key=True),
    sqlalchemy.Column("id_board", Integer, ForeignKey("boards.id_b")),
)
