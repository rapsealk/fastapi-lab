import threading
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_request():
    """
    [2022-03-21T14:21:16.401132] [GET /] Thread=22576
    INFO:     127.0.0.1:8407 - "GET / HTTP/1.1" 200 OK
    [2022-03-21T14:21:21.415086] [GET /] Thread=22576
    INFO:     127.0.0.1:8407 - "GET / HTTP/1.1" 200 OK
    [2022-03-21T14:21:26.422624] [GET /] Thread=22576
    INFO:     127.0.0.1:8407 - "GET / HTTP/1.1" 200 OK
    """
    print(f'[{datetime.now().isoformat()}] [GET /] Thread={threading.get_ident()}')
    i = 0
    for j in range(100000000):
        i += j
    return {"timestamp": datetime.now().isoformat(), "value": i}


@app.get("/async")
async def get_async_request():
    """
    [2022-03-21T14:21:41.166506] [GET /async] Thread=15972
    INFO:     127.0.0.1:8408 - "GET /async HTTP/1.1" 200 OK
    [2022-03-21T14:21:46.179180] [GET /async] Thread=15972
    INFO:     127.0.0.1:8408 - "GET /async HTTP/1.1" 200 OK
    [2022-03-21T14:21:51.183283] [GET /async] Thread=15972
    INFO:     127.0.0.1:8408 - "GET /async HTTP/1.1" 200 OK
    """
    print(f'[{datetime.now().isoformat()}] [GET /async] Thread={threading.get_ident()}')
    i = 0
    for j in range(100000000):
        i += j
    return {"timestamp": datetime.now().isoformat(), "value": i}
