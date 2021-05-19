import os
import sys

from fastapi import FastAPI

import manaba

PATH = os.path.abspath('')
sys.path.append(PATH)


app = FastAPI()


@app.post("/post/get_tasks")
def post_get_tasks(
    userid: str,
    password: str
) -> manaba.Tasks:

    # {"userid": userid, "password": password}
    return manaba.get_tasks(userid, password)


if __name__ == "__main__":
    app.run()
