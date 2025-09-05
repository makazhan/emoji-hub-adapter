from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import emojis

app = FastAPI(title="Emoji Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emojis.router, prefix="/api/v1/emojis", tags=["emojis"])

@app.get("/")
def root():
    return {"message": "Emoji Hub backend is running"}
