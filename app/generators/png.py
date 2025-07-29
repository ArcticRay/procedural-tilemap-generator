from PIL import Image
from .perlin import generate_tilemap
from .colors import TILE_COLORS


def render_tilemap_png(
    width: int, height: int, biome: str, tile_size: int = 16
) -> bytes:
    grid = generate_tilemap(width, height, biome)
    img = Image.new("RGB", (width * tile_size, height * tile_size))
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            color = TILE_COLORS.get(tile, (255, 0, 255))  # magenta for Unknown
            for dy in range(tile_size):
                for dx in range(tile_size):
                    img.putpixel((x * tile_size + dx, y * tile_size + dy), color)
    # In‑Memory
    from io import BytesIO

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.getvalue()
