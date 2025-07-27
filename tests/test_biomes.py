import pytest
from app.generators.biomes import get_rules


def test_get_rules_valid():
    thresholds, tiles = get_rules("desert")
    assert isinstance(thresholds, dict)
    assert isinstance(tiles, dict)
    assert set(thresholds.keys()) == set(tiles.keys())


def test_get_rules_invalid():
    with pytest.raises(ValueError) as exc:
        get_rules("nonexistent")
    assert "Unknown biome" in str(exc.value)
