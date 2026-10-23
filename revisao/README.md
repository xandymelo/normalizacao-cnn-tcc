# Revisão da literatura

Protocolo: Planejamento da Metodologia, seção 3.3 ([`docs/planejamento-metodologia.pdf`](../docs/planejamento-metodologia.pdf)).

| Arquivo | Conteúdo |
| --- | --- |
| [`busca_bibliografica.ipynb`](busca_bibliografica.ipynb) | Busca no OpenAlex com a *string* ampla e a do recorte, validação com o *seed set*, triagem por metadados (critérios I1–I3, E1–E3). Executado em 15/10/2026, com as saídas salvas |
| [`triagem_pesquisa_bibliografica.csv`](triagem_pesquisa_bibliografica.csv) | Os 299 registros triados, com metadados, critérios e decisão |
| [`fluxo_selecao.csv`](fluxo_selecao.csv) | Número de registros em cada etapa da seleção |
| [`conjunto_base.csv`](conjunto_base.csv) | Os 12 artigos do conjunto base (5 do *seed set* e 7 de periódicos), com DOI e papel na pesquisa |
| [`analise_conjunto_base.md`](analise_conjunto_base.md) | Análise individual, síntese comparativa, *insights* e justificativa da metodologia |

Os PDFs dos artigos não são versionados, por direitos autorais; use os DOIs para acessá-los.

**Pendente:** executar a mesma *string* na Scopus, no IEEE Xplore e na Web of Science, pelo Portal de Periódicos da CAPES, e salvar as exportações em `revisao/exportacoes/`; carregar a lista Qualis em `revisao/qualis.csv`. O notebook já lê esses arquivos.
