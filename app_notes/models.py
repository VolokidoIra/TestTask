import sqlalchemy
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, func

from database import metadata


notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id_n", Integer, primary_key=True),
    sqlalchemy.Column("text", Text),
    sqlalchemy.Column("date_created", DateTime, default=func.now()),
    sqlalchemy.Column("date_update", DateTime, default=func.now(), onupdate=func.now()),
)


note_statistic = sqlalchemy.Table(
    "note_statistic",
    metadata,
    sqlalchemy.Column("id_n", ForeignKey("notes.id_n"), primary_key=True),
    sqlalchemy.Column("views", Integer)
)
