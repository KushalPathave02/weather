from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router

app = FastAPI(title="AI Weather Assistant")

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://weather-wwxx.onrender.com",  # Deployed frontend URL
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
