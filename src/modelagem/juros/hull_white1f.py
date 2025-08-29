\"\"\"Simulação simples da taxa curta Hull-White 1F: dr = a(θ(t)-r)dt + σ dW.\"\"\"
import numpy as np

def simular_taxa_curta(r0: float, a: float, sigma: float, dt: float, n_passos: int, theta: float=0.0) -> np.ndarray:
    if n_passos <= 0 or dt <= 0 or sigma < 0 or a < 0:
        raise ValueError("parâmetros inválidos.")
    r = np.empty(n_passos+1) ; r[0] = r0
    for t in range(n_passos):
        dw = np.sqrt(dt)*np.random.randn()
        r[t+1] = r[t] + a*(theta - r[t])*dt + sigma*dw
    return r
