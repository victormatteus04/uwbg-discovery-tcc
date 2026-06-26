# UWBG Discovery TCC

Repositório de apoio ao Trabalho de Conclusão de Curso sobre descoberta assistida de materiais bidimensionais com `bandgap` largo a ultralargo (WBG/UWBG).

Página em formato de artigo: https://victormatteus04.github.io/uwbg-discovery-tcc/

O conteúdo reúne o pipeline computacional usado para treinar modelos MEGNet, comparar domínios `bulk`/2D, caracterizar candidatos UWBG, gerar novas composições por substituição química e avaliar o efeito de relaxação estrutural com M3GNet.

## Escopo

Este repositório foi organizado para servir como referência pública do TCC. Ele inclui:

- notebooks dos experimentos principais;
- funções auxiliares compartilhadas;
- relatórios por etapa;
- figuras e artefatos finais leves;
- checkpoints/modelos pequenos necessários para consulta dos resultados;
- documentação metodológica.

Dados brutos grandes ou com redistribuição não tratada diretamente no TCC foram deixados fora do Git. As instruções estão em [`data/README.md`](data/README.md).

## Estrutura

```text
.
├── 01_pretrain/                 # Pré-treino MEGNet em Materials Project
├── 02_finetune_c2db/            # Treino scratch e fine-tune no C2DB
├── 03_bulk2d_analysis/          # Análise pareada bulk-2D
├── 04_domain_gap/               # Avaliação de diferença de domínio
├── 05_inference_screening/      # Inferência e triagem UWBG
├── 06_residual_correction/      # Correção residual tabular
├── 07_uwbg_characterization/    # Caracterização química dos candidatos
├── 08_guided_generation/        # Geração guiada e relaxação M3GNet
├── data/                        # Dados leves e instruções para dados brutos
├── figures/                     # Figuras de apoio
├── models/                      # Modelo M3GNet local usado na relaxação
├── runs/                        # Relatórios, figuras, outputs e checkpoints
├── common.py                    # Utilitários compartilhados
├── METODOLOGIA_TCC.md           # Descrição metodológica detalhada
└── RELATORIO_FINAL.md           # Relatório consolidado dos resultados
```

## Ordem de execução

Os notebooks foram organizados para execução sequencial:

1. `01_pretrain/megnet_pretrain_mp.ipynb`
2. `02_finetune_c2db/megnet_finetune_c2db.ipynb`
3. `03_bulk2d_analysis/bulk2d_paired_analysis.ipynb`
4. `04_domain_gap/megnet_domain_analysis.ipynb`
5. `05_inference_screening/inference_comparison.ipynb`
6. `06_residual_correction/residual_correction.ipynb`
7. `07_uwbg_characterization/uwbg_characterization.ipynb`
8. `08_guided_generation/guided_generation.ipynb`

Os notebooks tiveram as saídas limpas para publicação. Os resultados consolidados permanecem em `runs/` e nos relatórios Markdown.

## Ambiente

O ambiente original foi executado com Python e bibliotecas de materiais/aprendizado de máquina, incluindo `matgl`, `pymatgen`, `ase`, `pandas`, `numpy`, `scikit-learn`, `torch` e `lightning`.

Um arquivo [`requirements.txt`](requirements.txt) foi incluído como referência aproximada. Dependendo da GPU/CUDA e da versão local do PyTorch, pode ser necessário ajustar a instalação.

## Dados excluídos do Git

Os seguintes arquivos foram usados localmente, mas não foram versionados:

- `data/mp.2019.04.01.json` — base local do Materials Project, aproximadamente 4 GB;
- `data/raw/c2db.db` — base SQLite local do C2DB, aproximadamente 74 MB.

Esses arquivos devem ser obtidos a partir das respectivas fontes originais e posicionados nos caminhos indicados para reexecução completa.

## Resultado resumido

O pipeline final:

- treinou modelos MEGNet para predição de `bandgap`;
- comparou desempenho entre treino direto no C2DB e transferência a partir do Materials Project;
- avaliou candidatos UWBG no C2DB;
- extraiu tendências químicas associadas a altos `bandgaps`;
- gerou candidatos por substituição guiada;
- separou materiais conhecidos de novas composições por fórmula reduzida e `layer group`;
- aplicou relaxação M3GNet a candidatos selecionados;
- organizou resultados para priorização de cálculos DFT posteriores.

Detalhes quantitativos estão em [`RELATORIO_FINAL.md`](RELATORIO_FINAL.md).

## Observação sobre reprodutibilidade

Este repositório documenta o pipeline e preserva os principais artefatos leves. A reexecução completa exige os dados brutos locais e ambiente compatível com as bibliotecas de grafos/materials informatics usadas no projeto.

## Código de terceiros

A pasta `vendor/matgl_src/` contém uma cópia local de parte do código do MatGL usada no projeto para isolar a etapa de relaxação M3GNet. Esse código é de autoria do Materials Virtual Lab e está sob licença BSD-3-Clause, preservada em [`vendor/matgl_src/LICENSE`](vendor/matgl_src/LICENSE).
