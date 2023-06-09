from app_board import schema
from app_board.models import boards, note_on_board
from app_notes.serializers import get_notes_by_board
from database import database

from logger import logger


async def create_board(board: schema.BoardCreate) -> bool:
    try:
        new_board_qr = boards.insert().values(title=board.title)
        await database.execute(new_board_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def get_board(board_id) -> dict:
    try:
        board_data: dict = dict(await database.fetch_one(boards.select().where(boards.c.id_b == board_id)))
        board_data['notes']: list = await get_notes_by_board(board_id=board_id)
    except Exception as e:
        logger.error(f"{e}")
        return {}

    return board_data


async def update_board(board: schema.BoardUpdate, board_id: int) -> bool:
    try:
        upd_board_qr = boards.update().where(boards.c.id_b == board_id).values(title=board.title)
        await database.execute(upd_board_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def delete_board(board_id: int) -> bool:
    try:
        unpin_qr = note_on_board.delete().where(note_on_board.c.id_board == board_id)
        await database.execute(unpin_qr)
        del_board_qr = boards.delete().where(boards.c.id_b == board_id)
        await database.execute(del_board_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def pin_note(note_id: int, board_id: int) -> bool:
    try:
        pin_note_rq = note_on_board.insert().values(id=note_id, id_board=board_id)
        await database.execute(pin_note_rq)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True


async def unpin_note(note_id: int, board_id: int) -> bool:
    try:
        unpin_note_qr = f"""DELETE FROM note_on_board WHERE (id={note_id} and id_board={board_id})"""
        await database.fetch_all(unpin_note_qr)
    except Exception as e:
        logger.error(f"{e}")
        return False

    return True
