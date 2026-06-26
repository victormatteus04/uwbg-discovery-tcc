# Figura 04 - Escala de bandgap e limiar UWBG

## Status

Criar figura nova.

## Diretrizes visuais

- Reduzir o texto dentro da figura ao mínimo necessário; detalhes devem ir na legenda ou no texto do TCC.
- Não usar emojis. Se precisar de marcação visual, usar ícones simples, setas, cores ou símbolos científicos.
- Não criar blocos finais de resumo, checklist ou explicações longas dentro da figura.
- Priorizar leitura rápida: poucas etapas, rótulos curtos, boa hierarquia visual e espaçamento amplo.

## Regra de conteúdo do prompt

- Este markdown deve conter toda a informação necessária para criar a figura corretamente.
- Nem toda informação deste markdown deve virar texto dentro da figura; a imagem deve mostrar a informação por composição visual, rótulos curtos, números essenciais e legenda.
- Quando houver muitos detalhes, separar: o que aparece como desenho, o que aparece como rótulo curto, o que aparece como número e o que deve ficar somente na legenda ou no texto do TCC.

## Onde entra no TCC

Introdução ou fundamentação teórica, logo após definir materiais de bandgap largo e ultra largo.

## Objetivo

Corrigir visualmente a definição usada no texto: neste TCC, materiais UWBG são tratados como materiais com bandgap acima de aproximadamente `3.4 eV`, conforme referência adotada.

## Mensagem principal

O limiar de referência para UWBG no trabalho é `Eg > 3.4 eV`. Esse valor deve substituir qualquer limiar anterior incorreto usado como critério de definição.

## Layout recomendado

Criar uma escala horizontal de `0` a `12 eV`, com marcadores para materiais conhecidos e uma linha vertical destacada em `3.4 eV`.

Use três regiões visuais:

- `Semicondutores convencionais`: abaixo de aproximadamente `3.4 eV`.
- `UWBG`: acima de `3.4 eV`.
- `Extremos de alto gap`: acima de `8 eV`, destacando os casos de interesse deste trabalho.

## Diagrama base

```text
0 eV ---------------- 3.4 eV ---------------- 8 eV -------- 12 eV
       convencionais | UWBG                    alto gap
                     ^
              limiar UWBG
```

## Informação que a figura deve mostrar

- Escala de bandgap de `0` a `12 eV`.
- Linha vertical no limiar `3.4 eV`.
- Região UWBG acima de `3.4 eV`.
- Materiais de referência distribuídos na escala.
- Se usados, LiF e BaF2 marcados como DFT externo deste trabalho, não treino.

## Texto que pode aparecer na figura

- `Eg (eV)`
- `3.4 eV`
- `UWBG`
- nomes curtos dos materiais de referência.

Explicações sobre origem dos valores devem ficar na legenda.

## Elementos visuais obrigatórios

- Eixo horizontal `Bandgap, Eg (eV)`.
- Linha vertical em `3.4 eV`.
- Rótulo explícito: `limiar UWBG adotado: 3.4 eV`.
- Marcadores de referência.

## Materiais de referência sugeridos

Usar valores aproximados apenas como orientação visual:

- Si: `~1.1 eV`.
- GaAs: `~1.4 eV`.
- SiC: `~3.3 eV`.
- GaN: `~3.4 eV`.
- beta-Ga2O3: `~4.8-4.9 eV`.
- Diamante: `~5.5 eV`.
- h-BN: `~6 eV`.
- AlN: `~6.2 eV`.

Se fizer sentido na versão final, adicionar os dois pontos externos calculados neste TCC:

- BaF2, DFT externo: `7.53 eV`.
- LiF, DFT externo: `8.46 eV`.

Esses dois pontos devem estar marcados como validação externa do trabalho, não como parte do treino.

## Cuidados

- Não usar outro valor como limiar de definição UWBG.
- Não misturar valores PBE, HSE e experimentais sem indicar a origem.
- Se houver valores experimentais, indicar isso na legenda.
- Se usar LiF e BaF2, dizer explicitamente que são resultados DFT externos usados para comparação.
