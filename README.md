# Modelagem

Repositório central de **modelos quantitativos** (crédito, derivativos, econometria) do WN Gaggiato.

## Estrutura
- \src/\: código-fonte, organizado por domínio (credit, derivatives, econometrics) e submodelos.
- \
otebooks/\: demonstrações e análises exploratórias.
- \data/\: dados brutos (\aw\) e tratados (\processed\). **Evite** subir dados sensíveis.
- \docs/\: documentação adicional.
- \	ests/\: testes automatizados (pytest).

## Como instalar (modo desenvolvimento)
Requer Python 3.11+ (recomendado):
\\\ash
python -m venv .venv
. .venv/Scripts/Activate.ps1  # PowerShell
pip install -r requirements.txt
pip install -e .
pytest
\\\

## Modelos incluídos (exemplos)
- Crédito: Merton (estrutural), Vasicek (PD/portfólio), Gordy ASRF (capital Basel), RAROC.
- Derivativos: Swaps, Opções, XVA (CVA/FVA/KVA).
- Econometria: VAR/VECM, GARCH.

