from fastapi import FastAPI
import uvicorn
import requests

from domain import *

app = FastAPI()

@app.get("/")
def get_data():
    return {"msg": "Not implemented yet."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5002)
