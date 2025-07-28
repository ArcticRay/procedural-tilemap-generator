from fastapi import APIRouter, Query, HTTPException
from app.models.map_request import MapRequest
from app.generators.perlin import generate_tilemap

router = APIRouter()


@router.post("/")
def generate_map(req: MapRequest):
    grid = generate_tilemap(req.width, req.height, req.biome)
    return {"map": grid}


@router.get("/")
def generate_map_get(
    width: int = Query(..., gt=0, description="Tilemap width"),
    height: int = Query(..., gt=0, description="Tilemap height"),
    biome: str = Query(..., description="Biome name"),
):
    try:
        grid = generate_tilemap(width, height, biome)
    except ValueError as e:
        # Return 422 for false Biome
        raise HTTPException(status_code=422, detail=str(e))
    return {"map": grid}
