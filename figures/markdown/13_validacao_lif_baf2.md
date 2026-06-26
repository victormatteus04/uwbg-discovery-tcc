# Figura 13 - Validação externa com LiF e BaF2

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

Resultados e discussão, na seção de comparação com DFT externo. A figura deve ser usada para mostrar o efeito da relaxação nos dois casos calculados fora do conjunto de treino.

## Objetivo

Comparar o bandgap predito antes e depois da relaxação com os valores DFT externos para LiF e BaF2.

## Mensagem principal

Nos dois casos, a predição em estrutura não relaxada superestimava o DFT externo. Após relaxação com M3GNet e reavaliação com MEGNet, o erro diminuiu fortemente.

## Layout recomendado

Usar dois painéis lado a lado:

1. `LiF`.
2. `BaF2`.

Em cada painel, usar um gráfico de pontos ou barras com três valores:

- `MEGNet original`.
- `MEGNet pós-relaxação`.
- `DFT externo`.

O DFT externo deve aparecer como linha ou marcador de referência.

## Diagrama base

```text
LiF:   MEGNet original -> MEGNet relaxado -> DFT externo
BaF2:  MEGNet original -> MEGNet relaxado -> DFT externo
```

Preferir gráfico de pontos conectados ou barras agrupadas. Usar poucos rótulos: valor em eV e erro, sem textos interpretativos longos dentro da figura.

## Dados a usar

LiF:

- Gap predito original: `9.624 eV`.
- Gap DFT externo: `8.460 eV`.
- Erro original: `+1.164 eV`.
- Gap pós-relaxação: usar o valor final presente nos resultados, aproximadamente `8.414 eV` se confirmado.
- Erro pós-relaxação: aproximadamente `-0.046 eV` se confirmado.

BaF2:

- Gap predito original: `8.177 eV`.
- Gap DFT externo: `7.530 eV`.
- Erro original: `+0.647 eV`.
- Gap pós-relaxação: usar o valor final presente nos resultados, aproximadamente `7.431 eV` se confirmado.
- Erro pós-relaxação: aproximadamente `-0.099 eV` se confirmado.

## Elementos visuais obrigatórios

- Valores em eV acima dos pontos ou barras.
- Seta mostrando redução do erro após relaxação.
- Classe de novidade:
  - `LiF`: `known_composition_new_layergroup`.
  - `BaF2`: `known_material`.
- Nota visual: `DFT externo não usado no treino`.

## Texto interno sugerido

- `Antes da relaxação`
- `Após relaxação`
- `DFT externo`
- `erro reduzido`

## Cuidados

- Não apresentar dois pontos como validação estatística ampla.
- Não misturar esses valores no dataset de treino.
- Destacar que ambos foram úteis como diagnóstico de geração/relaxação.
- Confirmar os valores pós-relaxação diretamente nos resultados finais antes de desenhar a versão definitiva.
