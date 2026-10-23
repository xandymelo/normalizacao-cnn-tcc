# Testes automatizados

Executados com `pytest` localmente e pelo GitHub Actions a cada envio.

**Existentes**

- `test_sortear_ordem.py` — o sorteio reproduz exatamente a ordem versionada em `experimento/ordem_execucao.csv`.

**Previstos com o código** (Planejamento do Experimento, seção 6.7)

- dada uma entrada aleatória, cada camada de normalização produz saída com média próxima de zero e variância próxima de um sobre o conjunto de valores esperado;
- dada a mesma semente, duas execuções curtas produzem as mesmas perdas e os mesmos pesos;
- dadas as quatro técnicas, as redes diferem apenas na camada de normalização;
- dada uma perda não finita simulada, a execução é interrompida e marcada como divergente;
- dada a divisão de uma semente, treino e validação não compartilham imagens e preservam a proporção das classes.
