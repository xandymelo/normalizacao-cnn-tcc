# Código do experimento (previsto para o mês 2)

Módulos planejados, conforme o Planejamento do Experimento (seções 6 e 7):

| Módulo | Responsabilidade |
| --- | --- |
| `dados.py` | Download do Fashion-MNIST, divisão estratificada treino/validação por semente, padronização |
| `modelos.py` | CNN de três blocos e fábrica das camadas de normalização (BatchNorm2d, GroupNorm com 1 e 8 grupos, Identity) |
| `treino.py` | Laço de treinamento, parada antecipada, restauração dos melhores pesos, detecção de divergência |
| `metricas.py` | Acurácia, F1 macro, épocas até a meta, medição de tempo (com sincronização da GPU) e de memória |
| `registro.py` | Gravação de `execucoes.csv` e `epocas.csv` e retomada após interrupção |
| `executar.py` | Execução das rodadas na ordem de `experimento/ordem_execucao.csv` |

Todos os valores vêm de [`experimento/config.yaml`](../../experimento/config.yaml); nada é fixado no código.
