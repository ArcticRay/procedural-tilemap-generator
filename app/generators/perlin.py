from noise import pnoise2


def generate_tilemap(w, h, biome):
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            n = pnoise2(x / 10, y / 10)
            if n < -0.05:
                row.append("water")
            elif n < 0.2:
                row.append("sand")
            else:
                row.append("rock")
        grid.append(row)
    return grid
