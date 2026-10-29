
import pytest

from basics import gc_percent, parse_counts


def test_gc_boundary():
    result = gc_percent(0, 20, 30, 0)
    assert result == 100.0


def test_gc_zero_total():
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


def test_invalid_counts():
    with pytest.raises(ValueError):
        parse_counts("10 20 -5 30")
