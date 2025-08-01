from .perlin import generate_tilemap
from .colors import TILE_COLORS


def render_tilemap_svg(width: int, height: int, biome: str, tile_size: int = 16) -> str:
    grid = generate_tilemap(width, height, biome)
    w_px = width * tile_size
    h_px = height * tile_size
    # SVG-Header
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{w_px}" height="{h_px}" viewBox="0 0 {w_px} {h_px}">'
    ]
    # quads
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            col = TILE_COLORS.get(tile, (255, 0, 255))
            hexcol = "#{:02x}{:02x}{:02x}".format(*col)
            px = x * tile_size
            py = y * tile_size
            lines.append(
                f'<rect x="{px}" y="{py}" '
                f'width="{tile_size}" height="{tile_size}" '
                f'fill="{hexcol}"/>'
            )
    lines.append("</svg>")
    return "\n".join(lines)
