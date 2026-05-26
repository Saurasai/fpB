from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.get('/home')
def home():
    return 'hello world'