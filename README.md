# Procedural Tilemap Generator Service

**FastAPI** microservice for procedural generation of 2D tilemaps with configurable biome rulesets, live-reload development, and multiple export formats.

[![CI](https://github.com/arcticray/procedural-tilemap-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/arcticray/procedural-tilemap-generator/actions/workflows/ci.yml)

---

## 🚀 Features

- **REST API Endpoints**
  - `POST  /generate_map/` → JSON tile grid
  - `GET   /generate_map/` → JSON via query params
  - `GET   /generate_map/png` → PNG image
  - `GET   /generate_map/svg` → SVG vector map
  - `GET   /generate_map/tmx` → TMX file for Tiled
- **Biome Ruleset**
  - External `biomes.yaml` defines thresholds & variants
  - Validates input, returns 422 on unknown biome
- **Variability**
  - Randomized noise offsets → every request yields a fresh map
- **Playground UI**
  - Interactive form, live PNG preview, download SVG/TMX buttons
- **Dockerized**
  - **Dev** image: live‐reload (`uvicorn --reload`), mounted code & config
  - **Prod** image: lean, excludes dev tools & tests
- **Testing & Linting**
  - `pytest` for unit/integration tests
  - `flake8`, `isort`, **Black** for style enforcement
- **CI/CD**
  - GitHub Actions: tests → lint → build dev & prod images

---

## 🖼️ Example Maps

**32×32 (forest)**  
![32x32 Forest](examples/map-32x32-forest.png)

**32×32 (desert)**  
![32x32 Desert](examples/map-32x32-desert.png)

---
