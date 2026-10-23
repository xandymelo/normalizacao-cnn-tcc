"""Testes do sorteio da ordem de execução (Planejamento do Experimento, seção 5.2 e Apêndice A)."""
import csv
from pathlib import Path

from experimento.sortear_ordem import cenarios, ordem_de_execucao, para_csv

RAIZ = Path(__file__).resolve().parents[1]


def test_given_4_tecnicas_e_2_lotes_when_montar_cenarios_then_ha_8_cenarios_com_lote_16_primeiro():
    c = cenarios()
    assert len(c) == 8
    assert c[0] == {"id": "C1", "tecnica": "Batch Normalization", "lote": 16}
    assert c[7] == {"id": "C8", "tecnica": "Sem normalização", "lote": 128}


def test_given_a_mesma_semente_when_sortear_duas_vezes_then_as_ordens_sao_identicas():
    assert ordem_de_execucao(2026) == ordem_de_execucao(2026)


def test_given_8_cenarios_e_5_sementes_when_sortear_then_cada_execucao_aparece_uma_vez():
    ids = [e["execucao"] for e in ordem_de_execucao(2026)]
    assert len(ids) == 40
    assert len(set(ids)) == 40


def test_given_a_semente_2026_when_sortear_then_a_ordem_bate_com_o_csv_versionado():
    with open(RAIZ / "experimento" / "ordem_execucao.csv", encoding="utf-8") as f:
        esperado = [linha["execucao"] for linha in csv.DictReader(f)]
    assert [e["execucao"] for e in ordem_de_execucao(2026)] == esperado


def test_given_a_ordem_sorteada_when_exportar_csv_then_reproduz_o_arquivo_versionado():
    versionado = (RAIZ / "experimento" / "ordem_execucao.csv").read_text(encoding="utf-8")
    assert para_csv(ordem_de_execucao(2026)) == versionado
