import asyncio

from fastapi import APIRouter, HTTPException, Response

from app_notes import serializers as srl_note, schema as sch_note
from app_board import serializers as srl_board, schema as sch_board

from logger import logger

api = APIRouter()


@api.get("/note/get_note/", response_model=sch_note.Note, status_code=200)
async def get_note(note_id: int):
    logger.info(f"Request to get note by id={note_id}")
    try:
        data = await asyncio.wait_for(srl_note.get_note(note_id=note_id), timeout=3.0)

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error get note by id={note_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error get note by id={note_id}")

    if not data:
        logger.error(f"Not found note by id={note_id}")
        raise HTTPException(status_code=404, detail=f"Not found note by id={note_id}")

    return data


@api.post("/note/create/", status_code=200)
async def create_note(note: sch_note.NoteCreate):
    logger.info(f"Request to create note")
    try:
        db_result = await asyncio.wait_for(srl_note.create_note(note=note), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error create note: {e}")
        raise HTTPException(status_code=504, detail=f"Error create note")

    return {}


@api.put("/note/update/", status_code=200)
async def update_note(note: sch_note.NoteUpdate, note_id: int):
    logger.info(f"Request to update note by id = {note_id}")
    try:
        db_result = await asyncio.wait_for(srl_note.update_note(note=note, note_id=note_id), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error update note by id={note_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error update note by id = {note_id}")

    return {}


@api.delete("/note/delete/", status_code=200)
async def delete_note(note_id: int):
    logger.info(f"Request to delete note by id = {note_id}")
    try:
        db_result = await asyncio.wait_for(srl_note.delete_note(note_id=note_id), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error delete note by id = {note_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error delete note by id = {note_id}")

    return {}


@api.get("/board/get_board/", status_code=200)
async def get_board(board_id: int):
    logger.info(f"Request to get board by id = {board_id}")
    try:
        data = await asyncio.wait_for(srl_board.get_board(board_id=board_id), timeout=3.0)

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error get board by id={board_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error get note by id={board_id}")

    if not data:
        logger.error(f"Not found board by id={board_id}")
        raise HTTPException(status_code=404, detail=f"Not found note by id={board_id}")

    return data


@api.post("/board/create/", status_code=200)
async def create_board(board: sch_board.BoardCreate):
    logger.info(f"Request to create board")
    try:
        db_result = await asyncio.wait_for(srl_board.create_board(board=board), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error create board: {e}")
        raise HTTPException(status_code=504, detail=f"Error create board")

    return {}


@api.put("/board/update/", status_code=200)
async def update_board(board: sch_board.BoardUpdate, board_id: int):
    logger.info(f"Request to update board by id = {board_id}")
    try:
        db_result = await asyncio.wait_for(srl_board.update_board(board=board, board_id=board_id), timeout=3.0)
        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error update board by id = {board_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error update board by id = {board_id}")

    return {}


@api.delete("/board/delete/", status_code=200)
async def delete_board(board_id: int):
    logger.info(f"Request to delete board by id = {board_id}")
    try:
        db_result = await asyncio.wait_for(srl_board.delete_board(board_id=board_id), timeout=3.0)
        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error delete board by id = {board_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error delete board by id = {board_id}")

    return {}


@api.post("/board/pin_note/", status_code=200)
async def pin_note(board_id: int, note_id: int):
    logger.info(f"Request to pin note {note_id} on board {board_id}")
    try:
        db_result = await asyncio.wait_for(srl_board.pin_note(board_id=board_id, note_id=note_id), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error pin note {note_id} on board {board_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error pin note {note_id} on board {board_id}")

    return {}


@api.delete("/board/unpin_note/", status_code=200)
async def unpin_note(board_id: int, note_id: int):
    logger.info(f"Request to unpin note {note_id} on board {board_id}")
    try:
        db_result = await asyncio.wait_for(srl_board.unpin_note(board_id=board_id, note_id=note_id), timeout=3.0)

        if not db_result:
            raise Exception

    except asyncio.TimeoutError:
        logger.error("DB responding time is out")
        raise HTTPException(status_code=504, detail=f"DB responding time is out")
    except Exception as e:
        logger.error(f"Error unpin note {note_id} on board {board_id}: {e}")
        raise HTTPException(status_code=504, detail=f"Error unpin note {note_id} on board {board_id}")

    return {}


