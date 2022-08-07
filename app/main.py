from fastapi import FastAPI
import config

app = FastAPI()
# settings = config.get_settings()


@app.get("/")
def homepage():
    return {"message": "Hello World"}
