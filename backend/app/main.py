from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import requests
import os

app = FastAPI()

# Path to frontend files
FRONTEND_PATH = os.environ.get("FRONTEND_BUILD_DIR", "/app/frontend")

# --- API ROUTE ---
@app.get("/api/emojis")
def get_emojis():
    resp = requests.get("https://emojihub.yurace.pro/api/all")
    if resp.status_code == 200:
        return resp.json()
    return {"error": "Failed to fetch emojis"}

# --- FRONTEND ROUTES ---
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))

@app.get("/emojis.html")
async def serve_emojis_page():
    return FileResponse(os.path.join(FRONTEND_PATH, "emojis.html"))

# --- OPTIONAL: fallback for unknown routes ---
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    index_path = os.path.join(FRONTEND_PATH, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Page not found"}
