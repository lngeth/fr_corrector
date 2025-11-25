from fastapi import FastAPI
from models import TextRequest
from routers import grammar

app = FastAPI()

app.include_router(grammar.router)