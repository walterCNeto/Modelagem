from modelagem.juros.hull_white1f import simular_taxa_curta
import numpy as np
def test_hw_tamanho():
    r = simular_taxa_curta(r0=0.12, a=0.1, sigma=0.01, dt=1/252, n_passos=100)
    assert isinstance(r, np.ndarray) and r.shape[0] == 101
