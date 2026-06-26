# Figura 03 - Bandgap direto e indireto

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

Fundamentação teórica, na seção de propriedades eletrônicas e bandgap.

## Objetivo

Explicar a definição visual de bandgap e a diferença entre gap direto e indireto em diagramas de bandas.

## Mensagem principal

O bandgap é a separação energética entre o máximo da banda de valência e o mínimo da banda de condução. Quando esses extremos ocorrem no mesmo ponto do espaço recíproco, o gap é direto; quando ocorrem em pontos diferentes, o gap é indireto.

## Layout recomendado

Use dois painéis lado a lado:

1. `Bandgap direto`.
2. `Bandgap indireto`.

Cada painel deve ter eixo vertical `Energia, E` e eixo horizontal `vetor de onda, k`.

## Diagrama base

```text
Painel A: gap direto
Eixo y: Energia
Eixo x: k
VBM e CBM no mesmo ponto k
Seta vertical Eg

Painel B: gap indireto
Eixo y: Energia
Eixo x: k
VBM e CBM em pontos k diferentes
Seta inclinada ou duas setas indicando diferença em k
```

## Informação que a figura deve mostrar

- Banda de valência e banda de condução.
- VBM e CBM.
- A distância energética `Eg`.
- A diferença visual entre VBM/CBM no mesmo `k` e em `k` diferente.
- Eixos `E` e `k`.

## Texto que pode aparecer na figura

- `Direto`
- `Indireto`
- `VBM`
- `CBM`
- `Eg`
- `E`
- `k`

A definição formal de `Eg` deve ficar na legenda ou no texto.

## Elementos visuais obrigatórios

- Banda de valência.
- Banda de condução.
- Máximo da banda de valência, `VBM`.
- Mínimo da banda de condução, `CBM`.
- Seta vertical indicando `Eg`.
- No painel indireto, VBM e CBM devem estar em pontos `k` diferentes.
- No painel direto, VBM e CBM devem estar alinhados no mesmo ponto `k`.

## Texto interno sugerido

- `Banda de valência`
- `Banda de condução`
- `VBM`
- `CBM`
- `E_g`
- `mesmo k`
- `k diferente`

## Fórmula a incluir

```tex
E_g = E_{\mathrm{CBM}} - E_{\mathrm{VBM}}
```

Legenda explicando:

- `Eg` é o bandgap.
- `E_CBM` é a energia no mínimo da banda de condução.
- `E_VBM` é a energia no máximo da banda de valência.

## Cuidados

- Não usar bandas complexas ou densas; a figura é conceitual.
- Não associar diretamente gap direto a "melhor" material, pois isso depende da aplicação.
- Não usar o limiar UWBG nesta figura; ele deve aparecer na figura da escala de bandgap.
