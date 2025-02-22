from fastapi import FastAPI
import requests
import uvicorn
import uuid
import time
from domain import *

MAX_RETRIES = 3
RETRY_DELAY = 2

processed_uuids = set()
messages = dict()

logging_url = "http://127.0.0.1:5001"
messages_url = "http://127.0.0.1:5002"

app = FastAPI()

@app.post("/")
def add_data(message: Message):
    uuid_val = uuid.uuid4()

    data = {"uuid": str(uuid_val), "msg": message.msg}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(logging_url, json=data, timeout=3)
            if response.status_code == 200:
                print("Message sent successfully")
                return
        except requests.exceptions.RequestException:
            print(f"Attempt {attempt}: Logging service unavailable. Retrying...")
            time.sleep(RETRY_DELAY)

    return {"msg": "success"}

@app.get("/")
def get_data():
    logging_response = requests.get(logging_url)
    messages_response = requests.get(messages_url)

    return {
        "Logging response": logging_response.json()["messages"],
        "Messages response": messages_response.json()["msg"]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
