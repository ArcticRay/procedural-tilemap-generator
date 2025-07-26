# Procedural Tilemap Generator Service

Lightweight FastAPI microservice for procedural generation of 2D tilemaps using Perlin noise.

## Current MVP

- **POST /generate_map/**
  - Parameters: `width`, `height`, `biome`
  - Returns: JSON grid of tiles (`water`, `sand`, `rock`)
- **Docker**
  - Dev & prod images, live reload in dev
- **Tests & Linting**
  - pytest suite, flake8, isort
- **CI**
  - GitHub Actions: tests, lint, Docker builds

## Planned Features

- **PNG export** via `/generate_map.png`
- **TMX export** for Tiled editors (.tmx)
- **Biome mixing** & additional noise algorithms
- **Spline‑based paths** for roads/rivers
- **Simple frontend** for live preview
- **Auth, caching, SDKs (Python/JS), Docker Hub/PyPI deployment**
