from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(title="AI Weather Assistant")

app.include_router(router)
