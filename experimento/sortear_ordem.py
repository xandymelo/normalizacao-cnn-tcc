"""Sorteia a ordem de execução das 40 rodadas do experimento.

Desenho fatorial 4 × 2 (técnica de normalização × tamanho do lote), cinco sementes por cenário.
A ordem é embaralhada por Fisher-Yates com o gerador mulberry32 e semente fixa, de modo que
o mesmo comando sempre produz o mesmo arquivo (Planejamento do Experimento, seção 5.2).

Uso: python -m experimento.sortear_ordem > experimento/ordem_execucao.csv
"""
import sys

TECNICAS = ["Batch Normalization", "Layer Normalization", "Group Normalization", "Sem normalização"]
LOTES = [16, 128]
SEMENTES = [0, 1, 2, 3, 4]
SEMENTE_SORTEIO = 2026
MASCARA = 0xFFFFFFFF


def cenarios():
    lista = []
    for lote in LOTES:
        for tecnica in TECNICAS:
            lista.append({"id": f"C{len(lista) + 1}", "tecnica": tecnica, "lote": lote})
    return lista


def _imul(a, b):
    return (a * b) & MASCARA


def mulberry32(semente):
    """Gerador pseudoaleatório de 32 bits; mesma semente, mesma sequência."""
    estado = semente & MASCARA

    def proximo():
        nonlocal estado
        estado = (estado + 0x6D2B79F5) & MASCARA
        t = _imul(estado ^ (estado >> 15), estado | 1)
        t ^= (t + _imul(t ^ (t >> 7), t | 61)) & MASCARA
        return ((t ^ (t >> 14)) & MASCARA) / 4294967296

    return proximo


def ordem_de_execucao(semente_sorteio=SEMENTE_SORTEIO):
    execucoes = [
        {"execucao": f"{c['id']}-S{s}", "cenario": c["id"], "tecnica": c["tecnica"], "lote": c["lote"], "semente": s}
        for c in cenarios()
        for s in SEMENTES
    ]
    aleatorio = mulberry32(semente_sorteio)
    for i in range(len(execucoes) - 1, 0, -1):  # Fisher-Yates
        j = int(aleatorio() * (i + 1))
        execucoes[i], execucoes[j] = execucoes[j], execucoes[i]
    return [{"ordem": i + 1, **e} for i, e in enumerate(execucoes)]


def para_csv(ordem):
    linhas = ["ordem,execucao,cenario,tecnica,lote,semente"]
    linhas += [f"{e['ordem']},{e['execucao']},{e['cenario']},{e['tecnica']},{e['lote']},{e['semente']}" for e in ordem]
    return "\n".join(linhas) + "\n"


if __name__ == "__main__":
    sys.stdout.write(para_csv(ordem_de_execucao()))
