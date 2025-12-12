from fastapi import FastAPI
from database import Query 

app = FastAPI()
db = Query()

@app.get('/api/v1/{user_id}/{note_id}')
async def api_read(user_id: int, note_id: int):
    try:
        note_date, note_text = await db.get_note(user_id, note_id)
        return {
                'user_id': user_id,
                'note_id': note_id,
                'note_date': note_date,
                'note_text': note_text,
                }

    except Exception as e:
        return {'error_message': e}


@app.delete('/api/v1/{user_id}/{note_id}')
async def api_delete(user_id: int, note_id: int):
    try:
        succeed = await db.delete_note(user_id, note_id)
        return {'status': succeed}
    except Exception as e:
        return {'error_message': e}


@app.post('/api/v1/{user_id}/create')
async def api_create(user_id: int, note_text: str, note_date: str):
    try:
        await db.ensure_user(user_id)
        new_note_id = await db.new_note(user_id, note_text, note_date)
        return {
                'user_id': user_id,
                'note_id': new_note_id,
                }
    except Exception as e:
        return {'error_message': e}

@app.update('/api/v1/{user_id}/{note_id}/update')
async def api_update(user_id: int, note_id: int, note_text: str):
    try:
        await db.update_note(user_id, note_id, note_text)
        return {
                'user_id': user_id,
                'note_id': note_id,
                'status': 'success',
        }
    except Exception as e:
        return {'error_message': e}
