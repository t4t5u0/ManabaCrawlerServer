# ManabaCrawlerServer
manaba を crawl する APIサーバ

## 起動手順

```bash
docker-compose up -d
```

or

```bash
git clone https://github.com/t4t5u0/ManabaCrawlerServer.git
cd ManabaCrawlerServer
pip install -r ./config/requirements.txt
./script/start.sh
```

## 停止時
```
docker-compose down
```

or

```bash
./script/stop.sh
```

## データ取得
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/post/get_tasks?userid=b1019206&password=bmnSrha7' \
  -H 'accept: application/json' \
  -d ''
```


[ManabaCrawlerServer/post_get_tasks.py at master · t4t5u0/ManabaCrawlerServer](https://github.com/t4t5u0/ManabaCrawlerServer/blob/master/post_get_tasks.py)より
```py
import requests
from pprint import pprint

import json

# input your information
user = {'userid': '', 'password': ''}
r = requests.post("http://127.0.0.1:8000/post/get_tasks",
                  params=user)  # POST user data

print(json.dumps(r.json(), ensure_ascii=False))
```
