\"\"\"Esqueleto de montagem de curva DI a partir de nós (prazo_dias, taxa_aa).\"\"\"
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Nodo:
    prazo_dias: int
    taxa_aa: float

def montar_curva(nodos: List[Nodo]) -> List[Tuple[int, float]]:
    \"\"\"Ordena e retorna [(prazo_dias, taxa_aa)].\"\"\"
    return sorted([(n.prazo_dias, n.taxa_aa) for n in nodos], key=lambda x: x[0])
