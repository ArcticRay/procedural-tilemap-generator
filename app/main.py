from fastapi import FastAPI
from app.api.v1 import router as api_v1
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Procedural Map Generator")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", include_in_schema=False)
def playground(
    request: Request,
    width: int = 16,
    height: int = 16,
    biome: str = "forest",
    tile_size: int = 16,
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "width": width,
            "height": height,
            "biome": biome,
            "tile_size": tile_size,
            "map_generated": True,
        },
    )


app.include_router(api_v1, prefix="/generate_map")
