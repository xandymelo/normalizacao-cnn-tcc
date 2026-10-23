# Efeito de técnicas de normalização sobre o treinamento de redes neurais convolucionais

Repositório da pesquisa do Trabalho de Conclusão de Curso de **Alexandre de Siqueira Melo Junior**, no Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

> **Estado atual:** planejamento concluído (versão `v0.1.0-planejamento`). O código do experimento será adicionado na etapa de implementação. A seção [Estado atual](#estado-atual) mostra o que já existe e o que está previsto.

## A pesquisa

**Questão de pesquisa.** Em uma rede neural convolucional de classificação de imagens, como Batch Normalization, Layer Normalization e Group Normalization, comparadas à ausência de normalização, afetam o desempenho preditivo, a velocidade de convergência, a estabilidade e o custo do treinamento sob diferentes tamanhos de lote?

**Experimento.** Desenho fatorial 4 × 2 — técnica de normalização × tamanho do lote (16 e 128) —, com cinco sementes por cenário, totalizando 40 execuções. Uma CNN compacta de três blocos convolucionais é treinada no Fashion-MNIST, e só a camada de normalização muda entre os cenários. São medidos acurácia e F1 no teste, épocas até 90% de acurácia de validação, tempo, memória e estabilidade.

Os documentos completos estão em [`docs/`](docs):

| Documento | Conteúdo |
| --- | --- |
| [Planejamento da metodologia](docs/planejamento-metodologia.pdf) | Caracterização da pesquisa, revisão da literatura, questão e hipóteses, visão geral do experimento, cronograma |
| [Planejamento do experimento](docs/planejamento-experimento.pdf) | Hipóteses estatísticas, variáveis, desenho, instrumentação, procedimento, coleta de dados, plano de análise, ameaças à validade |
| [Planejamento do repositório](docs/planejamento-repositorio.pdf) | Versão formal (ABNT) deste README |

## Objetivos deste repositório

1. **Reprodutibilidade** — permitir que qualquer pessoa refaça a busca bibliográfica e o experimento e obtenha os mesmos resultados.
2. **Rastreabilidade** — ligar cada resultado à versão exata do código, da configuração e do protocolo que o produziu.
3. **Transparência** — publicar o protocolo antes da coleta dos dados, para que nenhuma decisão de análise seja tomada depois de conhecidos os resultados.
4. **Preservação** — manter cópias seguras durante a pesquisa e arquivar a versão final com identificador permanente (DOI).

## Estrutura

```text
normalizacao-cnn-tcc/
├── README.md                  planejamento e guia do repositório (este arquivo)
├── LICENSE                    licença MIT do código
├── CITATION.cff               como citar o repositório
├── requirements.txt           dependências Python
├── pytest.ini                 configuração dos testes
├── .github/workflows/         integração contínua (testes a cada envio)
├── docs/                      planejamentos da pesquisa (PDF)
├── revisao/                   revisão da literatura
│   ├── busca_bibliografica.ipynb        busca no OpenAlex e triagem (executado)
│   ├── triagem_pesquisa_bibliografica.csv   299 registros triados com critérios I1–I3
│   ├── fluxo_selecao.csv                contagens de cada etapa da seleção
│   ├── conjunto_base.csv                12 artigos do conjunto base, com DOI
│   └── analise_conjunto_base.md         análise, síntese e insights
├── experimento/               definição do experimento
│   ├── config.yaml                      hiperparâmetros, fatores e sementes
│   ├── sortear_ordem.py                 sorteio reprodutível da ordem das execuções
│   └── ordem_execucao.csv               ordem das 40 execuções (Apêndice A do planejamento)
├── src/normalizacao/          código do experimento (dados, modelo, treino, métricas, registro)
├── testes/                    testes automatizados
├── notebooks/                 notebooks de piloto, execução e análise no Google Colab
├── resultados/                execucoes.csv e epocas.csv gerados pelo experimento
├── analise/                   scripts estatísticos e figuras
└── tcc/                       texto do TCC
```

Cada pasta ainda vazia tem um `README.md` que descreve o que ela vai conter.

## Estado atual

| Parte | Situação |
| --- | --- |
| Revisão da literatura (`revisao/`) | Concluída para a busca piloto no OpenAlex; busca nas bases CAPES pendente |
| Planejamentos (`docs/`) | Concluídos |
| Configuração e ordem do experimento (`experimento/`) | Concluídas e testadas |
| Código do experimento (`src/`) | Previsto para o mês 2 |
| Testes da implementação (`testes/`) | Testes do sorteio prontos; testes do modelo previstos com o código |
| Notebooks de execução (`notebooks/`) | Previstos para o mês 2 |
| Resultados e análise (`resultados/`, `analise/`) | Previstos para os meses 3 e 4 |
| Texto do TCC (`tcc/`) | Em elaboração, meses 1 a 6 |

## Como reproduzir

Requisitos: Python 3.9 ou superior e Git.

```bash
git clone https://github.com/xandymelo/normalizacao-cnn-tcc.git
cd normalizacao-cnn-tcc
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest                                   # executa os testes
python -m experimento.sortear_ordem      # reproduz experimento/ordem_execucao.csv
```

**Busca bibliográfica.** Abra [`revisao/busca_bibliografica.ipynb`](revisao/busca_bibliografica.ipynb) no Google Colab e execute todas as células. A API do OpenAlex pede uma chave gratuita para buscas maiores; cadastre-a nos *Secrets* do Colab com o nome `OPENALEX_API_KEY`. Como a base é atualizada continuamente, as contagens podem variar um pouco em relação às registradas (busca de 15/10/2026).

**Experimento.** Quando o código estiver disponível, a execução ocorrerá pelo notebook `notebooks/02_execucao.ipynb`, sempre a partir da tag `v1.0.0-protocolo`, que fixa o protocolo.

## O que é versionado

| Artefato | Versionado no Git? | Onde fica | Motivo |
| --- | --- | --- | --- |
| Código, testes, configuração, notebooks | Sim | `src/`, `testes/`, `experimento/`, `notebooks/` | Núcleo da reprodutibilidade |
| Planejamentos e texto do TCC | Sim | `docs/`, `tcc/` | Histórico das versões entregues |
| Resultados da busca bibliográfica | Sim | `revisao/` | Arquivos pequenos, base da triagem |
| Resultados do experimento (`execucoes.csv`, `epocas.csv`) | Sim | `resultados/` | Arquivos pequenos (poucos MB), base da análise |
| Figuras finais | Sim | `analise/figuras/` | Usadas no texto do TCC |
| Conjunto Fashion-MNIST | Não | Baixado pelo `torchvision` | Público e disponível; evita duplicar 30 MB |
| PDFs dos artigos | Não | Apenas DOI em `conjunto_base.csv` | Direitos autorais das editoras |
| Pesos dos modelos treinados | Não | Anexados à versão final (*release*) | Arquivos binários; não precisam de histórico |
| Chaves de API e credenciais | Nunca | Secrets do Colab | Segurança |

## Versionamento

**Ramos.** O ramo `main` contém sempre uma versão que passa nos testes. Cada mudança é feita num ramo curto (por exemplo, `feat/modelo-cnn` ou `fix/medicao-tempo`) e integrada ao `main` por *pull request*, depois que a integração contínua aprova os testes.

**Mensagens de commit.** Em português, no imperativo, com prefixo do tipo de mudança: `feat` (funcionalidade), `fix` (correção), `test` (testes), `docs` (documentação), `data` (dados ou resultados), `exp` (configuração do experimento), `analise` (análise estatística). Exemplo: `feat: adiciona camada de Group Normalization com 8 grupos`.

**Marcos.** Cada etapa da pesquisa termina com uma tag, que fixa o estado exato do repositório naquele momento:

| Tag | Marco | Quando |
| --- | --- | --- |
| `v0.1.0-planejamento` | Planejamentos da metodologia, do experimento e do repositório concluídos | Mês 1 |
| `v0.2.0-piloto` | Código implementado e testado; experimento piloto executado | Mês 2 |
| `v1.0.0-protocolo` | **Protocolo congelado.** Nenhuma alteração de código, hiperparâmetro ou critério depois desta tag | Mês 2, antes das 40 execuções |
| `v1.1.0-resultados` | 40 execuções concluídas e resultados versionados | Mês 3 |
| `v1.2.0-analise` | Análise estatística e figuras concluídas | Mês 4 |
| `v2.0.0-defesa` | Versão final do TCC, arquivada no Zenodo com DOI | Mês 6 |

A tag `v1.0.0-protocolo` funciona como um registro público do protocolo antes da coleta dos dados: qualquer mudança posterior fica visível no histórico.

## Integração contínua

A cada envio ao GitHub e a cada *pull request*, o GitHub Actions executa os testes automatizados ([`.github/workflows/testes.yml`](.github/workflows/testes.yml)). Hoje eles verificam o sorteio da ordem das execuções. Com o código do experimento, passam a verificar também as camadas de normalização, o determinismo com a mesma semente, a detecção de divergência e a divisão dos dados (Planejamento do Experimento, seção 6.7). Os testes rodam em CPU, com dados reduzidos; o treinamento completo roda no Google Colab com GPU.

## Cópias de segurança e preservação

São mantidas três cópias, em dois tipos de armazenamento e uma fora do computador: o computador do autor, o GitHub e o Google Drive. Este último recebe os resultados brutos durante as execuções no Colab, para que nada se perca se a sessão cair. Na versão final, o repositório é arquivado no [Zenodo](https://zenodo.org), integrado ao GitHub, que gera um DOI permanente para citação.

## Licenças

- **Código** (`src/`, `testes/`, `experimento/`, `analise/`, `notebooks/`): [MIT](LICENSE).
- **Textos, dados e figuras** (`docs/`, `revisao/`, `resultados/`, `tcc/`): [Creative Commons Atribuição 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt_BR).

## Como citar

Use os metadados de [`CITATION.cff`](CITATION.cff) (o GitHub mostra o botão *Cite this repository*). Depois da versão final, cite o DOI do Zenodo.

## Cronograma do repositório

| Mês | Atividades no repositório |
| --- | --- |
| 1 | Estrutura, README, licenças, revisão da literatura e planejamentos; tag `v0.1.0-planejamento` |
| 2 | Código, testes e notebooks; piloto (`v0.2.0-piloto`); congelamento do protocolo (`v1.0.0-protocolo`) |
| 3 | 40 execuções e versionamento dos resultados (`v1.1.0-resultados`) |
| 4 | Scripts de análise e figuras (`v1.2.0-analise`) |
| 5 | Texto do TCC: resultados, discussão e conclusão |
| 6 | Revisão final, versão de defesa e arquivamento no Zenodo (`v2.0.0-defesa`) |
