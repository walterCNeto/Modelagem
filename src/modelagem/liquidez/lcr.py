\"\"\"Indicador LCR simplificado: HQLA / Saídas Líquidas de Caixa em 30 dias.\"\"\"
def lcr(hqla: float, saidas_liquidas: float) -> float:
    if saidas_liquidas <= 0:
        raise ValueError("saidas_liquidas deve ser > 0.")
    if hqla < 0:
        raise ValueError("hqla não pode ser negativo.")
    return hqla / saidas_liquidas
