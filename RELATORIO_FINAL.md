# Relatorio final - Pipeline UWBG Discovery

## Escopo executado
A pasta `final/` foi validada como unidade autocontida de execucao: dados em `final/data`, notebooks em `final/01_*` a `final/08_*`, helper `final/common.py`, modelo M3GNet local em `final/models`, codigo MatGL vendorizado em `final/vendor` e artefatos em `final/runs`. Os treinos principais foram refeitos do zero no env `matgl-tcc`; a ultima rodada reexecutou o experimento 007 para incluir relaxacao M3GNet e relatorios atualizados.

## Metodologia
- Pre-treino MEGNet em Materials Project local (`000`).
- Treino C2DB scratch e fine-tune a partir do checkpoint MP local (`001`).
- Analise de pares bulk-2D para medir diferenca de dominio (`002`).
- Comparacao direta scratch vs fine-tune em dominio C2DB/HSE (`003`).
- Correcao residual tabular para calibrar predicoes (`004`).
- Inferencia/screening no subconjunto C2DB filtrado por `ehull <= 0.2 eV/atom` (`005`).
- Caracterizacao quimica UWBG e exportacao de filtros/classificadores (`006`).
- Geracao guiada por substituicao, classificacao de novidade e relaxacao M3GNet (`007`).

## Parametros e autocontencao
- `FORCE_RETRAIN=True` nos notebooks de treino executados do zero.
- Pre-treino: `MAX_EPOCHS=180`, `PATIENCE=30`, `BATCH_SIZE=64`.
- C2DB: `MAX_EPOCHS=360`, `PATIENCE_SCRATCH=35`, `PATIENCE_FINETUNE=35`.
- `USE_JARVIS=False`: nenhum dado/modelo JARVIS foi baixado ou usado.
- `USE_WANDB=False`: logs locais em `final/runs`.
- MEGNet de gap nos notebooks posteriores usa checkpoints gerados em `final/runs`.
- Relaxacao M3GNet usa `final/models/M3GNet-PES-MatPES-PBE-2025.2` e `final/vendor/matgl_src`, em subprocesso separado para nao alterar o `matgl` usado pelo MEGNet treinado.

## Resultados principais
- Pre-treino MP: melhor `val_MAE=0.3259` e `test_MAE=0.3574` eV.
- C2DB scratch: `test_MAE=0.3038` eV; C2DB fine-tune: `test_MAE=0.3243` eV.
- O scratch superou o fine-tune MP nesta execucao autocontida.
- Pares bulk-2D: 2046 totais, 456 com HSE.
- Correcao residual reduziu MAE de teste de 0.1767 para 0.1601 eV.
- A base local C2DB contem 16.905 entradas; o screening avaliou 9.627 materiais apos filtro termodinamico e marcou 1.529 como `UWBG_FT`.
- Caracterizacao classificou 1185 candidatos: {'TP': 780, 'Novel': 366, 'FP': 39}.
- Geracao guiada exportou 50 top candidatos novos, todos `new_composition`.
- Relaxacao M3GNet concluiu 90/90 estruturas selecionadas.

## Monitoramento de recursos
A GPU RTX 4060 Laptop de 8 GB foi monitorada durante os treinos. O pre-treino usou cerca de 2.3 GB de VRAM no pico observado; os treinos C2DB ficaram em torno de 0.5 GB. A etapa mais pesada em RAM foi o pareamento bulk-2D com o JSON MP, chegando a cerca de 21 GB usados, sem falha de memoria. Nao houve OOM.

## Relatorios por experimento
- [000 - Pre-treino MEGNet MP](runs/000_megnet_pretrain_mp/REPORT.md)
- [001 - Fine-tuning C2DB](runs/001_megnet_finetune_c2db/REPORT.md)
- [002 - Analise bulk-2D](runs/002_bulk2d_analysis/REPORT.md)
- [003 - Gap de dominio](runs/003_domain_gap/REPORT.md)
- [004 - Correcao residual](runs/004_residual_correction/REPORT.md)
- [005 - Inferencia screening](runs/005_inference_screening/REPORT.md)
- [006 - Caracterizacao UWBG](runs/006_uwbg_characterization/REPORT.md)
- [007 - Geracao guiada](runs/007_guided_generation/REPORT.md)

## Revisao de novidade pos-DFT
Os calculos DFT externos de LiF e BaF2 mostraram que o filtro antigo de novidade era permissivo: LiF e BaF2 nao devem ser tratados como descobertas novas. O experimento 007 foi corrigido para comparar formula reduzida e layergroup do prototipo contra o C2DB.
- `final/common.py` possui `build_c2db_material_index` e `classify_c2db_novelty`.
- LiF ficou como `known_composition_new_layergroup`; BaF2 ficou como `known_material` com match `1BaF2-2`.
- `top_novel_candidates.csv` usa somente composicoes ausentes no C2DB.
- `external_dft_comparison.csv` guarda LiF/BaF2 apenas para comparacao, sem uso no treino.
- Apos relaxacao M3GNet, LiF caiu de 9.624 para 8.414 eV contra DFT 8.460 eV; BaF2 caiu de 8.177 para 7.431 eV contra DFT 7.530 eV.

## Resultados do experimento 007
- Guiados totais: 697.
- `new_composition`: 323.
- `known_material`: 297.
- `known_composition_new_layergroup`: 77.
- `top_novel_candidates.csv`: 50 candidatos, todos `new_composition`.
- Amostras por faixa, todos candidatos: {'0-2': 10, '10-12': 7, '2-4': 10, '4-6': 10, '6-8': 10, '8-10': 10}.
- Amostras por faixa, novos: {'0-2': 10, '10-12': 5, '2-4': 10, '4-6': 10, '6-8': 10, '8-10': 7}.
- Relaxacao M3GNet: {'relaxed': 90}.
- Delta pos-relaxacao: media -0.801 eV, mediana -0.600 eV, faixa [-5.572, 3.345] eV.
- Casos relaxados ainda UWBG: 74/90; entre `new_composition`: 50/61.

## Interpretacao final
A correcao metodologica principal foi separar validacao de descoberta: materiais ja existentes no C2DB continuam uteis como controles por faixa de gap, mas nao entram no ranking de candidatos novos. A relaxacao M3GNet reduziu os gaps na media, reforcando que substituicoes em prototipos nao relaxados podem superestimar. Mesmo apos relaxacao, a maioria dos candidatos novos avaliados permaneceu na faixa UWBG, mas os casos com `substitution_risk=high` devem ser priorizados para DFT apenas apos inspeccao estrutural e estabilidade.

## Guidelines para reproducao
Execute os notebooks em ordem com o kernel `matgl-tcc`. Os caminhos sao resolvidos por `final/common.py`; outputs devem permanecer em `final/runs`. Para reexecutar do zero, limpe `final/runs/*` e execute `01` a `08`. Para o experimento 007, mantenha `final/models/M3GNet-PES-MatPES-PBE-2025.2` e `final/vendor/matgl_src`; o notebook isola esse M3GNet em subprocesso e preserva o MEGNet treinado no ambiente conda.
