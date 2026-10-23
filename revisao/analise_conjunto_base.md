UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO  
BACHARELADO EM SISTEMAS DE INFORMAÇÃO

**Disciplina:** Projetos para Sociedade II  
**Discente:** Alexandre de Siqueira Melo Junior

---

# ATIVIDADE 7 — CONJUNTO BASE DE ARTIGOS, ANÁLISE E SÍNTESE

## Enunciado

> Entregue os ficheiros dos artigos usados como conjunto base para a definição dos *insights*. Juntamente com os ficheiros, a análise e síntese feita para suportar e justificar a pesquisa e, por conseguinte, a escolha da metodologia a ser aplicada.

## 1. Formação do conjunto base

O conjunto base resulta da pesquisa bibliográfica registrada no notebook [`busca_bibliografica.ipynb`](busca_bibliografica.ipynb), executada em 15/10/2026 no OpenAlex, seguindo o protocolo das Atividades 3 e 5.

| Etapa | Registros |
| --- | --- |
| String do recorte, sem filtros | 7.380 |
| Artigos de periódico, 2015–2026 | 3.400 |
| Mais relevantes baixados para triagem | 300 |
| Após remoção de duplicatas | 299 |
| Excluídos por I3/E3 (sem indício de avaliação empírica) | 121 |
| Aprovados em I1 e I3, pendentes de verificação Qualis (I2) | 178 |

A leitura dos títulos e resumos dos 178 registros mostrou que a maioria **usa** Batch Normalization como componente de uma aplicação (diagnóstico médico, sensoriamento remoto, detecção de falhas), sem estudá-la. Por isso, aplicaram-se dois critérios adicionais para formar o conjunto base:

> **C1 — objeto de estudo:** a normalização é o objeto da avaliação — comparação entre técnicas, comparação com e sem normalização, ou análise do efeito da normalização sobre convergência, estabilidade ou custo.
>
> **C2 — acesso ao texto completo:** o artigo está disponível em acesso aberto, para que a análise se apoie no texto completo e o arquivo possa ser entregue.

Dez artigos de periódico atenderam a C1. Três deles não atenderam a C2 e ficaram fora (seção 7). Os **sete** restantes (A1–A7) se somam aos **cinco** trabalhos do *seed set* (S1–S5), que definem as técnicas comparadas no TCC, formando um conjunto base de **12 artigos**. Os *seeds* são anais de conferência ou *preprints* e, por isso, não atendem à regra Qualis (I2); entram como fundamentação, não como evidência da amostra.

## 2. Arquivos entregues

Os arquivos dos artigos não são versionados neste repositório, por direitos autorais; os identificadores de cada um estão em [`conjunto_base.csv`](conjunto_base.csv).

| ID | Trabalho | Veículo | Papel no TCC |
| --- | --- | --- | --- |
| S1 | Ioffe; Szegedy (2015) — *Batch Normalization* | ICML (anais) | Técnica comparada (BN) |
| S2 | Ba; Kiros; Hinton (2016) — *Layer Normalization* | arXiv | Técnica comparada (LN) |
| S3 | Wu; He (2018) — *Group Normalization* | ECCV (anais) | Técnica comparada (GN); efeito do lote |
| S4 | Singh; Krishnan (2020) — *Filter Response Normalization* | CVPR (anais) | Alternativa independente do lote |
| S5 | Brock et al. (2021) — *Image Recognition Without Normalization* | ICML (anais) | Condição sem normalização |
| A1 | Mishkin; Sergievskiy; Matas (2017) — *Systematic evaluation of CNN advances on the ImageNet* | Computer Vision and Image Understanding | Avaliação sistemática; BN, ativação e tamanho do lote |
| A2 | Ma; Klabjan (2024) — *Diminishing Batch Normalization* | IEEE Transactions on Neural Networks and Learning Systems | Convergência; comparação BN × LN |
| A3 | Wu et al. (2019) — *L1-Norm Batch Normalization* | IEEE Transactions on Neural Networks and Learning Systems | Custo computacional da BN |
| A4 | Kazimi; Sandfeld (2025) — *Batch Normalization and Instance Normalization* (TEM) | Microscopy and Microanalysis | Comparação direta entre técnicas, com repetições |
| A5 | Fagbohungbe; Qian (2022) — *Effect of Batch Normalization on Noise Resistant Property* | IEEE Access | Com e sem BN; efeito colateral |
| A6 | Nguyen; Choi; Yang (2023) — *EUNNet* | IEEE Access | Treino estável sem normalização |
| A7 | Kathayat; Akurathi; Thalla (2025) — *CNNs with and Without Batch Normalization* | Global J. of Engineering Innovations and Interdisciplinary Research | Desenho mais próximo do TCC |

A1, A2, A3 e A5 são as versões dos autores depositadas no arXiv; A4, A6 e A7 são as versões publicadas.

## 3. Análise individual

### 3.1 *Seed set* — técnicas que o TCC compara

| ID | Ideia central | Evidência relevante para o TCC |
| --- | --- | --- |
| S1 | Normaliza cada ativação com média e variância do **mini-lote**, seguida de escala e deslocamento aprendidos. | Permite taxas de aprendizado maiores e reduz o número de passos de treino no ImageNet. Depende do tamanho do lote. |
| S2 | Calcula as estatísticas sobre as unidades da **mesma camada**, em cada exemplo. | Não depende do lote e faz o mesmo cálculo no treino e no teste. Os autores relatam desempenho inferior à BN em redes convolucionais. |
| S3 | Calcula as estatísticas por **grupos de canais**; LN e Instance Normalization são casos particulares. | Com lote 32, fica a 0,5 ponto da BN; com lote 2, tem 10,6 pontos de erro a menos que a BN. |
| S4 | Normaliza cada filtro de cada exemplo, sem subtrair a média, com ativação de limiar aprendido (TLU). | Mantém a acurácia de 32 até 1 imagem por GPU, enquanto a BN degrada. |
| S5 | Treina ResNets **sem normalização**, com *adaptive gradient clipping*. | Mostra que a ausência de normalização é uma condição de comparação legítima, desde que o treino seja estabilizado. |

### 3.2 Artigos de periódico

**A1 — Mishkin; Sergievskiy; Matas (2017).** Avaliação sistemática de escolhas de arquitetura e treinamento de CNNs no ImageNet, variando **um fator por vez**. Sobre normalização: o melhor posicionamento da BN, antes ou depois da ativação, se inverte entre arquiteturas (CaffeNet × GoogLeNet); a BN apaga as diferenças entre variantes da ReLU; e a ativação muda o efeito da BN (Sigmoid com BN supera ReLU sem BN, mas Tanh com BN fica abaixo de Sigmoid com BN). Sobre o lote: manter a taxa de aprendizado constante ao mudar o tamanho do lote prejudica o desempenho, e lotes de 512 ou mais reduzem a acurácia. Os autores também mostram que imagens de 128 × 128 pixels bastam para conclusões qualitativas sobre a estrutura da rede, com custo uma ordem de grandeza menor.

**A2 — Ma; Klabjan (2024).** Propõe a *Diminishing Batch Normalization*, que atualiza os parâmetros da BN por média móvel decrescente, e apresenta a primeira análise de convergência para BN. Nos experimentos (MNIST, CIFAR-10, CIFAR-100 e outros), com lote de 100, supera a BN original e a Layer Normalization. É uma das poucas comparações entre BN e LN publicadas em periódico.

**A3 — Wu et al. (2019).** Mede o **custo** da BN. Na tabela de vazão do artigo, inserir BN reduz as amostras processadas por segundo em 31,9% (ResNet-110), 31,6% (DenseNet-100) e 20,6% (MobileNet). Propõe a normalização por norma L1, com acurácia e velocidade de convergência equivalentes às da BN convencional e maior eficiência em hardware. Confirma que o ganho de convergência da normalização tem um custo por iteração que precisa ser medido.

**A4 — Kazimi; Sandfeld (2025).** Compara Batch Normalization e Instance Normalization em U-Net e ResNet para segmentação de imagens de microscopia eletrônica, em dois conjuntos de dados. A Instance Normalization supera a BN de forma consistente em Dice e IoU. Os autores justificam o resultado pelo fato de a Instance Normalization calcular as estatísticas por imagem, o que a torna mais adequada quando a variação entre imagens é alta ou o lote é pequeno. Metodologicamente, é o estudo mais rigoroso do conjunto: **cada experimento é executado cinco vezes**, e os resultados são reportados como média e erro-padrão.

**A5 — Fagbohungbe; Qian (2022).** Treina ResNet44 e VGG16 com e sem BN em CIFAR-10 e CIFAR-100 e injeta ruído analógico nos pesos. Com BN, a acurácia normalizada sob ruído cai para 41,32% (ResNet44) e 10,75% (VGG16), contra 91,95% e 93,80% sem BN. O impacto cresce com o número de camadas BN. A análise teórica do artigo associa lotes maiores a menor resistência a ruído. Mostra que a normalização pode ter **efeitos colaterais** além da acurácia.

**A6 — Nguyen; Choi; Yang (2023).** Propõe uma camada convolucional que permite treinar ResNets sem normalização usando os mesmos hiperparâmetros das redes normalizadas, com desempenho igual ou superior em reconhecimento de imagens, detecção e segmentação. Os autores apontam que os métodos anteriores sem normalização exigem ajuste fino de hiperparâmetros e que as NF-ResNets (S5) não são estáveis com lotes grandes. Reforça que a condição **sem normalização** é instável quando nada a compensa.

**A7 — Kathayat; Akurathi; Thalla (2025).** Compara a mesma CNN com e sem BN (Adam, taxa de aprendizado 0,001, lote 64, 50 a 100 épocas), medindo acurácia, perda, tempo de treinamento e épocas até a convergência. Com BN: acurácia de teste de 90,5% contra 84,7%, 2.800 s contra 3.500 s de treino e convergência em 35 contra 50 épocas. É o desenho mais próximo do TCC, mas tem limitações: compara apenas BN e ausência de normalização, usa um único tamanho de lote e **não informa repetições, sementes nem variabilidade** dos resultados.

## 4. Síntese comparativa

| ID | Técnicas comparadas | Arquitetura | Dados | Varia o lote? | Repetições | Acurácia | Convergência | Custo | Estabilidade |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | BN × sem | Inception | ImageNet, MNIST | Não | Não informa | ✓ | ✓ | — | ✓ |
| S2 | LN × BN × sem | RNNs, MLP | Vários | Sim (MNIST) | Não informa | ✓ | ✓ | — | ✓ |
| S3 | GN × BN × LN × IN | ResNet | ImageNet, COCO | **Sim (32 a 2)** | Não informa | ✓ | — | — | ✓ |
| S4 | FRN × BN × GN × LN × IN | ResNet, Inception | ImageNet, COCO | **Sim (32 a 1)** | Não informa | ✓ | — | — | ✓ |
| S5 | Sem × BN | NFNet, ResNet | ImageNet | Não | Não informa | ✓ | — | ✓ | ✓ |
| A1 | BN × sem; posição da BN; ativações | CaffeNet, GoogLeNet | ImageNet 128 px | **Sim** | Não informa | ✓ | — | ✓ | — |
| A2 | DBN × BN × LN | FNN, ResNet-18 | MNIST, CIFAR | Não (100) | Não informa | ✓ | ✓ | — | — |
| A3 | L1BN × BN × sem | ResNet, DenseNet, MobileNet | CIFAR, ImageNet | Não | Não informa | ✓ | ✓ | **✓** | — |
| A4 | IN × BN | U-Net, ResNet | Imagens de microscopia | Não | **5 execuções, média ± erro-padrão** | ✓ | — | — | — |
| A5 | BN × sem | ResNet44, VGG16 | CIFAR-10/100 | Não | Não informa | ✓ | — | — | ✓ (ruído) |
| A6 | Sem (EUNConv) × BN | ResNet | ImageNet, COCO | Não | Não informa | ✓ | — | — | ✓ |
| A7 | BN × sem | CNN simples | MNIST, CIFAR-10 | Não (64) | **Não** | ✓ | ✓ | ✓ | — |

✓ = desfecho medido; — = não medido ou não identificado na leitura.

## 5. *Insights*

1. **Não existe técnica de normalização universalmente superior.** A vantagem depende do tamanho do lote (S3, S4), da arquitetura (S2, A1), da tarefa e dos dados (A4) e da função de ativação (A1). Isso confirma o tema do TCC: a escolha da normalização é uma decisão que precisa de evidência, não um padrão automático.

2. **O tamanho do lote é o fator que mais muda a comparação.** A BN degrada com lotes pequenos, enquanto GN, LN e FRN não dependem do lote (S3, S4). A1 mostra que o próprio lote afeta a acurácia, A5 relaciona o lote à robustez do modelo treinado e A6 relata instabilidade de redes sem normalização com lotes grandes. Logo, comparar normalizações com um único lote, como em A7, leva a uma conclusão parcial.

3. **A normalização acelera a convergência, mas custa por iteração.** A BN reduz o número de épocas até a meta (S1, A7), mas diminui a vazão de treino em 20% a 32% (A3). Medir só a acurácia final esconde essa troca, então o TCC deve medir épocas até a meta, tempo total e memória.

4. **A ausência de normalização é uma condição válida, mas instável.** S5 e A6 mostram que é possível treinar sem normalização com técnicas compensatórias; sem elas, o treino exige ajuste fino (A6). A condição sem normalização é, portanto, o grupo de controle natural, e a estabilidade (divergência, variação entre execuções) deve ser medida explicitamente.

5. **Os efeitos dependem de outros fatores, que precisam ser fixados.** O posicionamento da BN e a função de ativação mudam o resultado (A1). Uma comparação justa muda só a normalização e mantém todo o resto igual, como fez A1.

6. **Há uma lacuna nas comparações publicadas em periódicos.** A maioria dos 178 registros aprovados só usa BN como componente. Entre os que a estudam, as comparações diretas com várias técnicas estão principalmente nos anais de conferência (S3, S4) e foram feitas em larga escala (ImageNet, COCO), com recursos que um TCC não tem. Os estudos em periódico com desenho acessível comparam no máximo duas condições (A4, A5, A7), e só A4 repete os experimentos e relata a variabilidade. **Falta uma comparação controlada, reprodutível e em pequena escala de BN, LN, GN e ausência de normalização, sob tamanhos de lote diferentes, com repetições e medição de custo.**

7. **Pequena escala é suficiente para conclusões qualitativas.** A1 mostra que imagens reduzidas preservam as conclusões sobre a estrutura da rede, com custo uma ordem de grandeza menor. Isso sustenta um experimento com dados pequenos e hardware acessível.

## 6. Justificativa da metodologia

O TCC adota uma **pesquisa experimental, quantitativa e comparativa**, com **desenho fatorial controlado**. Cada decisão do desenho responde a um *insight*:

| Decisão metodológica | Justificativa | Base |
| --- | --- | --- |
| Experimento controlado, mudando só a normalização | O efeito da normalização se confunde com ativação e posição da camada; é preciso isolá-lo. | Insight 5; A1 |
| Técnicas: BN, LN, GN e sem normalização | Cobrem os três eixos de estatística (lote, camada, grupo de canais) e o grupo de controle. | Insights 1 e 4; S1–S3, S5 |
| Fator lote: 16 e 128 | A dependência do lote é o principal diferencial entre BN e as alternativas. | Insight 2; S3, S4, A1 |
| CNN compacta (3 blocos convolucionais, ReLU), mesma em todos os cenários | Fixa arquitetura e ativação, que alteram o efeito da BN. | Insight 5; A1 |
| Dataset Fashion-MNIST | Classificação de imagens com custo baixo; conclusões qualitativas se mantêm em pequena escala. | Insight 7; A1 |
| 5 sementes por cenário (40 execuções) e média ± desvio-padrão | Segue o único estudo acessível com repetições (cinco execuções) e corrige a principal falha dos demais: resultados de uma única execução. | Insight 6; A4, A7 |
| Métricas: acurácia e F1 macro no teste; épocas e tempo até 90% de acurácia de validação; memória máxima; execuções divergentes ou `NaN` | Medem as quatro dimensões do problema: desempenho, convergência, custo e estabilidade. O F1 corresponde ao Dice usado em A4. | Insights 3 e 4; A3, A4, A7 |
| Equivalência: diferença de até 1 ponto percentual de acurácia; desempate por custo e estabilidade | Evita declarar vencedora uma técnica por diferenças dentro da variação entre sementes. | Insights 1 e 3 |

Esse desenho preenche a lacuna do *insight* 6: compara mais técnicas que os estudos em periódico com escala acessível (A4, A5, A7), varia o tamanho do lote e repete cada cenário, com recursos de um computador pessoal ou do Google Colab.

## 7. Limitações do conjunto base

- **Artigos sem acesso ao texto completo.** Três artigos de periódico atenderam ao critério C1, mas exigem assinatura e não puderam ser obtidos; ficaram fora do conjunto base e não sustentam nenhum *insight*:
  - GARBIN; ZHU; MARQUES (2020), *Dropout vs. batch normalization: an empirical study of their impact to deep learning*. DOI: 10.1007/s11042-019-08453-9.
  - PENG; YU; YU (2024), *Re-thinking the effectiveness of batch normalization and beyond*. DOI: 10.1109/TPAMI.2023.3319005.
  - MACÊDO *et al.* (2019), *Enhancing batch normalized convolutional networks using displaced rectifier linear units: a systematic comparative study*. DOI: 10.1016/j.eswa.2019.01.066.
- A busca foi feita no OpenAlex. As bases do Periódicos CAPES (Scopus, IEEE Xplore, Web of Science) ainda serão consultadas com a mesma string, o que pode acrescentar artigos ao conjunto.
- A verificação Qualis (I2) está pendente para todos os artigos de periódico.
- A triagem considerou os 300 registros mais relevantes, não os 3.400.

## Referências

BA, J. L.; KIROS, J. R.; HINTON, G. E. Layer normalization. **arXiv preprint**, arXiv:1607.06450, 2016.

BROCK, A. *et al.* High-performance large-scale image recognition without normalization. *In*: INTERNATIONAL CONFERENCE ON MACHINE LEARNING, 38., 2021. **Proceedings** […]. PMLR, 2021. v. 139, p. 1059-1071.

FAGBOHUNGBE, O.; QIAN, L. The effect of batch normalization on noise resistant property of deep learning models. **IEEE Access**, v. 10, p. 127728-127741, 2022. DOI: 10.1109/ACCESS.2022.3206958.

IOFFE, S.; SZEGEDY, C. Batch normalization: accelerating deep network training by reducing internal covariate shift. *In*: INTERNATIONAL CONFERENCE ON MACHINE LEARNING, 32., 2015. **Proceedings** […]. PMLR, 2015. v. 37, p. 448-456.

KATHAYAT, K.; AKURATHI, L. P. R.; THALLA, U. Comparing the performance of convolutional neural networks with and without batch normalization. **Global Journal of Engineering Innovations and Interdisciplinary Research**, v. 5, n. 6, 2025. DOI: 10.33425/3066-1226.1178.

KAZIMI, B.; SANDFELD, S. Enhancing semantic segmentation in high-resolution TEM images: a comparative study of batch normalization and instance normalization. **Microscopy and Microanalysis**, v. 31, n. 1, ozae093, 2025. DOI: 10.1093/mam/ozae093.

MA, Y.; KLABJAN, D. Diminishing batch normalization. **IEEE Transactions on Neural Networks and Learning Systems**, v. 35, n. 5, p. 6544-6557, 2024. DOI: 10.1109/TNNLS.2022.3210840.

MISHKIN, D.; SERGIEVSKIY, N.; MATAS, J. Systematic evaluation of convolution neural network advances on the Imagenet. **Computer Vision and Image Understanding**, v. 161, p. 11-19, 2017. DOI: 10.1016/j.cviu.2017.05.007.

NGUYEN, K.-B.; CHOI, J.; YANG, J.-S. EUNNet: efficient un-normalized convolution layer for stable training of deep residual networks without batch normalization layer. **IEEE Access**, v. 11, p. 76977-76988, 2023. DOI: 10.1109/ACCESS.2023.3244072.

SINGH, S.; KRISHNAN, S. Filter response normalization layer: eliminating batch dependence in the training of deep neural networks. *In*: IEEE/CVF CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION, 2020. **Proceedings** […]. IEEE, 2020. p. 11234-11243. DOI: 10.1109/CVPR42600.2020.01125.

WU, S. *et al.* L1-norm batch normalization for efficient training of deep neural networks. **IEEE Transactions on Neural Networks and Learning Systems**, v. 30, n. 7, p. 2043-2051, 2019. DOI: 10.1109/TNNLS.2018.2876179.

WU, Y.; HE, K. Group normalization. *In*: EUROPEAN CONFERENCE ON COMPUTER VISION, 2018. **Proceedings** […]. Cham: Springer, 2018. p. 3-19. (Lecture Notes in Computer Science). DOI: 10.1007/978-3-030-01261-8_1.
