from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# bind: can execute SQL statements and is a connection or engine

@app.get('/')
async def create_database():
    return {'Database':'Created'}