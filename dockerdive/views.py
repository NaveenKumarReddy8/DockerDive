from fastapi import FastAPI

from dockerdive import __version__

app = FastAPI()


@app.get("/")
def index():
    return {"Name": "DockerDive", "Version": __version__}
