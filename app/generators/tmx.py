import xml.etree.ElementTree as ET
from io import BytesIO
from app.generators.perlin import generate_tilemap


def render_tilemap_tmx(
    width: int, height: int, biome: str, tile_size: int = 32
) -> bytes:
    grid = generate_tilemap(width, height, biome)

    map_attrib = {
        "version": "1.9",
        "tiledversion": "1.9.2",
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "width": str(width),
        "height": str(height),
        "tilewidth": str(tile_size),
        "tileheight": str(tile_size),
    }
    root = ET.Element("map", map_attrib)

    ET.SubElement(
        root,
        "tileset",
        {
            "firstgid": "1",
            "name": biome,
            "tilewidth": str(tile_size),
            "tileheight": str(tile_size),
        },
    )

    layer = ET.SubElement(
        root,
        "layer",
        {
            "name": "Tile Layer 1",
            "width": str(width),
            "height": str(height),
        },
    )
    data = ET.SubElement(layer, "data", {"encoding": "csv"})

    gid_map = {}
    next_gid = 1
    rows = []
    for row in grid:
        csv_row = []
        for tile in row:
            if tile not in gid_map:
                gid_map[tile] = next_gid
                next_gid += 1
            csv_row.append(str(gid_map[tile]))
        rows.append(",".join(csv_row))
    data.text = "\n" + "\n".join(rows) + "\n"

    # XML with Declaration
    tree = ET.ElementTree(root)
    buf = BytesIO()
    tree.write(buf, encoding="utf-8", xml_declaration=True)
    return buf.getvalue()
