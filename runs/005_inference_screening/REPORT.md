# Experimento 005 - Inferencia e screening C2DB

## Objetivo
Aplicar os modelos MEGNet treinados a todos os materiais C2DB disponiveis e organizar o screening UWBG.

## Resultados
- Materiais avaliados: 9627.
- Materiais com HSE conhecido: 3070.
- Candidatos `UWBG_FT` por fine-tune: 1529.
- Categorias mais frequentes: {'haleto': 2911, 'sulfeto': 1164, 'tiossal': 1141, 'seleneto': 1138, 'telureto': 1110}.
- Arquivo principal: `outputs/all_materials_predictions.csv`.

## Interpretacao
O screening cobre 9.627 materiais e separa predicoes scratch/fine-tune. A distribuicao e dominada por haletos, sulfetos e selenetos, com candidatos UWBG fortemente concentrados em quimicas com alta eletronegatividade, em linha com os filtros aprendidos no experimento 006.

## Figuras
- ![convergence_all](figures/convergence_all.png)
- ![error_violin_range](figures/error_violin_range.png)
- ![mae_bias_per_range](figures/mae_bias_per_range.png)
- ![oxide_coverage](figures/oxide_coverage.png)
- ![oxide_scatter_all_models](figures/oxide_scatter_all_models.png)
- ![oxide_scatter_delta](figures/oxide_scatter_delta.png)
- ![precision_recall_uwbg](figures/precision_recall_uwbg.png)
- ![scatter_all](figures/scatter_all.png)
- ![uwbg_screening_all](figures/uwbg_screening_all.png)
