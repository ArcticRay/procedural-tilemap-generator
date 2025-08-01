from fastapi import APIRouter, Query, HTTPException
from app.models.map_request import MapRequest
from app.generators.perlin import generate_tilemap
from fastapi.responses import Response
from app.generators.png import render_tilemap_png
from app.generators.tmx import render_tilemap_tmx

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


@router.get(
    "/png", response_class=Response, responses={200: {"content": {"image/png": {}}}}
)
def generate_map_png(
    width: int = Query(..., gt=0),
    height: int = Query(..., gt=0),
    biome: str = Query(...),
    tile_size: int = Query(16, gt=1),
):
    try:
        png_bytes = render_tilemap_png(width, height, biome, tile_size)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return Response(content=png_bytes, media_type="image/png")


@router.get(
    "/tmx",
    response_class=Response,
    responses={200: {"content": {"application/xml": {}}}},
)
def generate_map_tmx(
    width: int = Query(..., gt=0),
    height: int = Query(..., gt=0),
    biome: str = Query(...),
    tile_size: int = Query(32, gt=1),
):
    try:
        tmx_bytes = render_tilemap_tmx(width, height, biome, tile_size)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return Response(content=tmx_bytes, media_type="application/xml")
