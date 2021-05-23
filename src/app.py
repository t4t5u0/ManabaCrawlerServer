import os
import sys
import time

from fastapi import FastAPI


PATH = os.path.abspath('')
sys.path.append(PATH)

from src.manaba import manaba

app = FastAPI()


@app.post("/post/get_tasks")
def post_get_tasks(
    userid: str,
    password: str
) -> manaba.Tasks:

    # {"userid": userid, "password": password}
    time.sleep(0.5)
    return manaba.get_tasks(userid, password)


if __name__ == "__main__":
    app.run()
