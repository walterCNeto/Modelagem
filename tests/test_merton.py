from src.credit.merton.merton import pd_merton
import math

def test_pd_merton_monotonic():
    # PD deve aumentar com D (mais dívida => maior PD)
    pd1 = pd_merton(V0=100, D=80, r=0.05, sigma=0.25, T=1.0)
    pd2 = pd_merton(V0=100, D=120, r=0.05, sigma=0.25, T=1.0)
    assert pd2 > pd1

def test_pd_merton_params():
    # Valores válidos
    p = pd_merton(100, 100, 0.03, 0.2, 1.0)
    assert 0.0 <= p <= 1.0

def test_pd_merton_invalid():
    import pytest
    with pytest.raises(ValueError):
        pd_merton(0, 100, 0.03, 0.2, 1.0)
