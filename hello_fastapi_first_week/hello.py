from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get('/hello')
@app.get('/')
async def hello():
    return {'msg': 'Hello, world!'}

@app.get('/time')
async def time():
    return {"time": datetime.datetime.now().isoformat()}
