from noise import pnoise2
from .biomes import get_rules
import random


def generate_tilemap(w: int, h: int, biome: str):
    thresholds, tiles = get_rules(biome)
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            n = pnoise2(x / 10, y / 10)
            for tile_type, limit in thresholds.items():
                if n < limit:
                    choices = tiles[tile_type]
                    row.append(random.choice(choices))
                    break
        grid.append(row)
    return grid
