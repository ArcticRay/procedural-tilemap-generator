from noise import pnoise2
from .biomes import get_rules
import random


def generate_tilemap(w: int, h: int, biome: str):
    offset_x = random.random() * 1000
    offset_y = random.random() * 1000

    thresholds, tiles = get_rules(biome)

    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            n = pnoise2((x + offset_x) / 10, (y + offset_y) / 10)
            for tile_type, limit in thresholds.items():
                if n < limit:
                    choices = tiles[tile_type]
                    row.append(random.choice(choices))
                    break
        grid.append(row)
    return grid
