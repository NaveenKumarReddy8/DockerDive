from time import sleep

from fastapi import FastAPI
from redis import Redis

from dockerdive import __version__

app = FastAPI()

cache = Redis(host="redis", port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            sleep(0.5)


@app.get("/")
def index():
    return {"Name": "DockerDive", "Version": "0.2.0", "count": get_hit_count()}
