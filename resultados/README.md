# Resultados (previstos para o mês 3)

Gerados pelas 40 execuções do experimento. Os resultados do piloto ficam em `resultados/piloto/` e não entram na análise.

## `execucoes.csv` — uma linha por execução

| Coluna | Conteúdo |
| --- | --- |
| `ordem`, `execucao`, `cenario` | Posição na ordem sorteada e identificadores (por exemplo, `7`, `C3-S2`, `C3`) |
| `tecnica`, `lote`, `semente` | Níveis dos fatores e semente |
| `epocas_executadas`, `melhor_epoca` | Épocas treinadas e época restaurada |
| `epoca_meta` | Primeira época com acurácia de validação ≥ meta; vazio se não atingida |
| `tempo_medio_epoca_s`, `tempo_meta_s`, `tempo_total_s` | Tempos, em segundos |
| `memoria_max_mb` | Pico de memória alocada na GPU |
| `acc_teste`, `f1_macro_teste`, `perda_teste` | Desempenho no conjunto de teste |
| `divergiu` | 1 se houve perda não finita; 0 caso contrário |
| `gpu`, `versao_python`, `versao_torch`, `data_hora` | Ambiente e momento da execução |

## `epocas.csv` — uma linha por época

| Coluna | Conteúdo |
| --- | --- |
| `execucao`, `epoca` | Identificador da execução e número da época |
| `perda_treino`, `acc_treino` | Perda média e acurácia no treino |
| `perda_val`, `acc_val` | Perda e acurácia na validação |
| `tempo_epoca_s` | Tempo de treino da época, em segundos |

Codificação UTF-8, separador vírgula, ponto decimal.
