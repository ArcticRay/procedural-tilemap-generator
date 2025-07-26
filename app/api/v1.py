from fastapi import APIRouter
from app.models.map_request import MapRequest
from app.generators.perlin import generate_tilemap

router = APIRouter()

@router.post("/")
def generate_map(req: MapRequest):
    grid = generate_tilemap(req.width, req.height, req.biome)
    return {"map": grid}
