# Figura 01 - Materiais 2D: visão geral

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

Fundamentação teórica, antes da discussão de propriedades eletrônicas. A figura deve introduzir o que caracteriza um material bidimensional e por que a estrutura cristalina 2D é tratada de modo diferente de materiais bulk.

## Objetivo

Mostrar visualmente que um material 2D é periódico no plano e confinado na direção perpendicular. A figura deve ajudar o leitor a entender a transição entre material bulk, monocamada e representação usada em simulações.

## Mensagem principal

Materiais 2D preservam periodicidade em duas direções cristalográficas, mas têm espessura atômica e interação reduzida fora do plano. Em cálculos periódicos, isso normalmente é representado com uma célula contendo vácuo na direção perpendicular ao plano.

## Layout recomendado

Use uma figura horizontal em três blocos, com setas da esquerda para a direita:

1. Material bulk lamelar.
2. Exfoliação ou isolamento de uma monocamada.
3. Célula periódica 2D usada em cálculo ou banco de dados.

No terceiro bloco, desenhe os vetores de rede no plano, `a1` e `a2`, e a direção fora do plano, `z`, com uma região de vácuo explicitamente indicada.

## Diagrama base

```mermaid
flowchart LR
    A[Bulk lamelar] --> B[Monocamada 2D]
    B --> C[Célula periódica com vácuo]
```

## Informação que a figura deve mostrar

- O material bulk como várias camadas empilhadas.
- A separação de uma única camada.
- A monocamada com periodicidade no plano.
- A caixa de simulação com vácuo na direção `z`.
- Os vetores `a1` e `a2` no plano.
- A diferença visual entre plano periódico e direção fora do plano.

## Texto que pode aparecer na figura

- `Bulk`
- `Monocamada`
- `Célula 2D`
- `vácuo`
- `a1`, `a2`, `z`

Todo detalhamento conceitual deve ficar na legenda.

## Elementos visuais obrigatórios

- Bloco 3D com camadas empilhadas, representando o material bulk.
- Seta indicando separação de uma camada.
- Monocamada com átomos em rede periódica.
- Caixa de simulação com vácuo fora do plano.
- Eixos `x`, `y` e `z`.
- Texto curto indicando "periodicidade no plano" e "confinamento fora do plano".

## Exemplos visuais opcionais

Adicionar três miniaturas no rodapé:

- Grafeno: exemplo semimetálico.
- h-BN: exemplo isolante de alto bandgap.
- MoS2 ou outro TMD: exemplo semicondutor 2D.

Essas miniaturas devem ser apenas ilustrativas, não precisam entrar na metodologia.

## Texto interno sugerido

- `Bulk lamelar`
- `Monocamada 2D`
- `Célula periódica com vácuo`
- `a1`, `a2`
- `z / vácuo`

## Cuidados

- Não transformar a figura em revisão de literatura com muitos exemplos.
- Não usar valores numéricos de bandgap nesta figura.
- Evitar aparência de material molecular isolado; a periodicidade no plano deve ser clara.
