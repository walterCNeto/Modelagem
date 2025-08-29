from modelagem.credito.merton import pd_merton

def test_pd_merton_faixa():
    p = pd_merton(100, 100, 0.03, 0.2, 1.0)
    assert 0.0 <= p <= 1.0
