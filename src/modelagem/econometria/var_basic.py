\"\"\"Constrói matriz de lags (simples) para série em 1D.\"\"\"
import numpy as np

def construir_lags(x: np.ndarray, p: int) -> np.ndarray:
    x = np.asarray(x).reshape(-1)
    if p <= 0 or len(x) <= p:
        raise ValueError("defina p > 0 e série longa o bastante.")
    n = len(x) - p
    X = np.column_stack([x[i: i+n] for i in range(p, 0, -1)])
    return X
