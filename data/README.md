# Dados

Esta pasta contém apenas dados leves que podem ser mantidos no Git.

## Incluído

- `band_gap_no_structs.gz`: arquivo auxiliar leve usado no pipeline.

## Não incluído

Os arquivos abaixo foram usados localmente, mas não foram adicionados ao repositório público:

| Arquivo esperado | Motivo |
| --- | --- |
| `data/mp.2019.04.01.json` | Arquivo bruto grande do Materials Project, com aproximadamente 4 GB. |
| `data/raw/c2db.db` | Base SQLite local do C2DB. Deve ser obtida a partir da fonte original do C2DB. |

Para reexecutar o pipeline completo, obtenha esses arquivos nas fontes originais e coloque-os exatamente nesses caminhos.

```text
data/
├── mp.2019.04.01.json
└── raw/
    └── c2db.db
```

Os resultados já processados e relatórios principais permanecem em `runs/`.

