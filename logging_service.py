from fastapi import FastAPI
import uvicorn

from domain import *
app = FastAPI()

messages = dict()

@app.post("/")
def add_data(data: DataModel):
    if data.uuid in messages.keys():
        return {"msg": "duplication"}

    messages[data.uuid] = data.msg
    print(data.msg)

    return {"msg": "success"}


@app.get("/")
def get_data():
    return {"messages": [msg for msg in messages.values()]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
