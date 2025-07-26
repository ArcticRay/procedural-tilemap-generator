from app.generators.perlin import generate_tilemap


def test_size_and_values():
    w, h = 16, 16
    grid = generate_tilemap(w, h, "forest")

    assert isinstance(grid, list) and len(grid) == h
    assert all(isinstance(row, list) and len(row) == w for row in grid)

    allowed = {"water", "sand", "rock"}
    assert set(cell for row in grid for cell in row) <= allowed
