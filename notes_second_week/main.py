from fastapi import FastAPI
from database import Query # not implemented yet

app = FastAPI()
db = Query()

@app.get('/api/v1/{user_id}/{note_id}')
async def api_read(user_id: int, note_id: int):
    try:
        note_date, note_text = db.get_note(user_id, note_id)
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
        succeed = db.delete_note(user_id, note_id)
        return {'status': succeed}
    except Exception as e:
        return {'error_message': e}


@app.post('/api/v1/{user_id}/create')
async def api_create(user_id: int, note_text: str, note_date: str):
    try:
        new_note_id = db.new_note(user_id, note_text, note_date)
        return {
                'user_id': user_id,
                'note_id': new_note_id,
                }
    except Exception as e:
        return {'error_message': e}
