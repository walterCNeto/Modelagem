from modelagem.mercado.curva_di import montar_curva, Nodo

def test_montar_curva_ordena():
    nodos = [Nodo(252,0.12), Nodo(21,0.10), Nodo(504,0.13)]
    prazos = [p for p,_ in montar_curva(nodos)]
    assert prazos == sorted(prazos)
