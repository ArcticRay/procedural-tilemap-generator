from app.generators.perlin import generate_tilemap

import pytest


def test_size_and_values():
    grid = generate_tilemap(16, 16, "forest")
    assert len(grid) == 16
    assert all(len(row) == 16 for row in grid)
    allowed = {"water_stream", "grass", "forest_floor", "rock"}
    assert set(cell for row in grid for cell in row) <= allowed


@pytest.mark.parametrize("biome", ["desert", "forest", "tundra"])
def test_generator_all_biomes(biome):
    grid = generate_tilemap(8, 8, biome)
    assert len(grid) == 8


def test_generator_unknown_biome():
    with pytest.raises(ValueError):
        generate_tilemap(4, 4, "void")
