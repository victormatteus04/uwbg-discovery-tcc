# Figura 14 - Candidatos recomendados para validação DFT por faixa de gap

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

Resultados e conclusões, como ponte entre os resultados computacionais e trabalhos futuros/validação DFT.

## Objetivo

Mostrar uma seleção equilibrada de candidatos por faixa de bandgap, com ênfase em materiais que podem fortalecer as conclusões do TCC.

## Mensagem principal

A validação DFT não deve escolher apenas os maiores gaps. É mais informativo selecionar candidatos em faixas diferentes, com diferentes riscos de substituição e, quando possível, contendo oxigênio.

## Layout recomendado

Usar uma régua vertical ou horizontal de bandgap com faixas:

- `0-2 eV`.
- `2-4 eV`.
- `4-6 eV`.
- `6-8 eV`.
- `8-10 eV`.
- `10-12 eV`.

Em cada faixa, inserir de 1 a 3 candidatos representativos, coloridos por risco de substituição.

## Diagrama base

```text
0-2    | candidato controle
2-4    | candidato próximo ao limiar
4-6    | candidato UWBG moderado
6-8    | candidato intermediário-alto
8-10   | candidato extremo
10-12  | candidato extremo/limite
```

Usar no máximo 1 candidato destacado por faixa na figura principal. Candidatos adicionais podem ir em tabela no texto.

## Candidatos sugeridos

Usar estes candidatos como base, se continuarem presentes nos resultados finais:

- `MgAgF3`, `~0.371 eV`: controle negativo, não UWBG, útil para mostrar que o pipeline também rejeita candidatos.
- `SiPO3F`, `~3.241 eV`: próximo ao limiar, contém oxigênio, baixo risco.
- `SiPClO3`, `~4.016 eV`: faixa `4-6 eV`, contém oxigênio, baixo risco, recomendado para validação.
- `Hf3O5F2`, `~6.136 eV`: faixa `6-8 eV`, contém oxigênio, gap intermediário-alto, avaliar risco.
- `BOF`, `~9.502 eV`: faixa `8-10 eV`, contém oxigênio, candidato extremo.
- `BeB2F8`, `~10.858 eV`: faixa `10-12 eV`, gap muito alto, útil como teste de extrapolação.

## Elementos visuais obrigatórios

- Faixas de gap claramente marcadas.
- Marcador para limiar UWBG em `3.4 eV`.
- Cores por risco de substituição:
  - Verde: baixo.
  - Amarelo: médio.
  - Vermelho: alto.
- Ícone ou rótulo para presença de oxigênio.
- Indicação dos três candidatos prioritários finais para DFT.

## Priorização sugerida

Destacar como trio principal:

- `SiPClO3`: representa UWBG moderado logo acima do limiar e contém oxigênio.
- `Hf3O5F2`: representa faixa intermediária-alta e química de óxidos/fluoretos.
- `BOF` ou `BeB2F8`: representa extremo de alto gap; escolher o de menor risco ou maior coerência estrutural nos resultados finais.

## Cuidados

- Confirmar gaps e classes de novidade diretamente nas tabelas finais antes de desenhar.
- Não escolher apenas candidatos de alto gap, pois isso enfraquece a discussão metodológica.
- Separar candidatos novos de controles já conhecidos.
