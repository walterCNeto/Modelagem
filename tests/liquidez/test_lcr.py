from modelagem.liquidez.lcr import lcr
import pytest

def test_lcr_basico():
    assert lcr(100, 80) == 100/80

def test_lcr_valida():
    with pytest.raises(ValueError):
        lcr(100, 0)
