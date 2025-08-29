\"\"\"Modelo estrutural de Merton (versão simplificada).
Retorna PD em horizonte T, assumindo valor de firma lognormal.
\"\"\"
from math import log, sqrt
from scipy.stats import norm

def pd_merton(V0: float, D: float, r: float, sigma: float, T: float) -> float:
    \"\"\"Probabilidade de default no modelo de Merton.

    Parâmetros
    ----------
    V0 : float
        Valor presente dos ativos da firma
    D : float
        Dívida (valor de face no vencimento T)
    r : float
        Taxa livre de risco (contínua) ao ano
    sigma : float
        Volatilidade anual dos ativos
    T : float
        Horizonte (anos)

    Retorna
    -------
    float
        PD(T) = P(V_T < D)
    \"\"\"
    if any(x <= 0 for x in (V0, D, sigma, T)):
        raise ValueError("V0, D, sigma e T devem ser positivos.")
    muT = log(V0) + (r - 0.5 * sigma**2) * T
    sT = sigma * sqrt(T)
    # P(V_T < D) = P(ln V_T < ln D) = Phi((ln D - muT) / sT)
    z = (log(D) - muT) / sT
    return float(norm.cdf(z))
