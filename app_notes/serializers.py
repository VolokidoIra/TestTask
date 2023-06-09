from app_notes import schema
from database import database
from app_notes.models import notes, note_statistic
from app_board.models import note_on_board

from logger import logger


async def get_note(note_id: int) -> dict:
    try:
        get_note_qr = f"""
            SELECT note.id_n, note.text, note.date_created, note.date_update, st.views 
            FROM notes note 
            LEFT OUTER JOIN note_statistic st 
            on note.id_n = st.id_n
            where note.id_n = {note_id}"""
        data = await database.fetch_all(get_note_qr)

        update_views_gr = f"""UPDATE note_statistic SET views = views+1 WHERE id_n = {note_id}"""
        await database.fetch_all(update_views_gr)
    except Exception as e:
        logger.error(f"{e}")
        return {}

    return data[0]


async def create_note(note: schema.NoteCreate) -> bool:
    try:
        new_note_qr = notes.insert().values(text=note.text)
        note_id = await database.execute(new_note_qr)

        new_statistic_qr = note_statistic.insert().values(id_n=note_id, views=0)
        await database.execute(new_statistic_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def update_note(note: schema.NoteUpdate, note_id: int) -> bool:
    try:
        upd_note_qr = notes.update().where(notes.c.id_n == note_id).values(text=note.text)
        await database.execute(upd_note_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False
    return True


async def delete_note(note_id: int) -> bool:
    try:
        del_statistic_qr = note_statistic.delete().where(note_statistic.c.id_n == note_id)
        await database.execute(del_statistic_qr)

        unpin_qr = note_on_board.delete().where(note_on_board.c.id == note_id)
        await database.execute(unpin_qr)

        del_note_qr = notes.delete().where(notes.c.id_n == note_id)
        await database.execute(del_note_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def get_notes_by_board(board_id) -> list:
    try:
        notes_by_board_rq = f"""
        SELECT note.id_n, note.text, note.date_created, note.date_update, st.views 
        FROM notes note 
        LEFT OUTER JOIN note_statistic st 
        on note.id_n = st.id_n
        where note.id_n in 
            (SELECT id FROM note_on_board 
            where id_board={board_id})"""

        data = await database.fetch_all(notes_by_board_rq)
    except Exception as e:
        logger.error(f"{e}")
        return []

    return data
