from modelagem.econometria.var_basic import construir_lags
import numpy as np
import pytest

def test_lags_dim():
    x = np.arange(10.0)
    X = construir_lags(x, p=3)
    assert X.shape == (7, 3)

def test_lags_invalido():
    with pytest.raises(ValueError):
        construir_lags(np.arange(3.0), p=3)
