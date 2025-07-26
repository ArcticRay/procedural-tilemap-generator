from fastapi import FastAPI
from app.api.v1 import router as api_v1

app = FastAPI(title="Procedural Map Generator")
app.include_router(api_v1, prefix="/generate_map")
