\"\"\"PD no modelo estrutural de Merton (versão simples).\"\"\"
from math import log, sqrt
from scipy.stats import norm

def pd_merton(V0: float, D: float, r: float, sigma: float, T: float) -> float:
    if any(x <= 0 for x in (V0, D, sigma, T)):
        raise ValueError("V0, D, sigma, T devem ser positivos.")
    muT = log(V0) + (r - 0.5*sigma**2)*T
    sT = sigma*sqrt(T)
    z = (log(D) - muT)/sT
    return float(norm.cdf(z))
