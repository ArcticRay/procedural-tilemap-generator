import yaml
from pathlib import Path
from pydantic import ValidationError

# Load yaml once
_biomes_data = yaml.safe_load(Path("biomes.yaml").read_text())


def get_rules(biome: str):
    """Gibt (thresholds, tiles) für ein bekanntes Biome zurück.
    Bei unbekanntem Biome wird ein ValueError geworfen."""
    try:
        cfg = _biomes_data[biome]
    except KeyError:
        raise ValueError(f"Unknown biome: {biome}") from None

    thresholds = cfg.get("thresholds", {})
    tiles = cfg.get("tiles", {})

    if set(thresholds.keys()) != set(tiles.keys()):
        raise ValidationError(
            f"Inconsistent rules for biome '{biome}'", model=type(biome)
        )
    return thresholds, tiles
