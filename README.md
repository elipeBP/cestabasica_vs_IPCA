# Cesta Básica vs. IPCA

Modelagem de dados para comparar a variação de preços da cesta básica com a série histórica do IPCA — a base para cruzar preços coletados por web scraping com a inflação oficial.

## Schema (SQLAlchemy)

- **`ipca`** — série histórica mensal do índice IPCA (`data_referencia`, `indice_mensal`).
- **`categoria_item`** — categorias da cesta básica (ex.: arroz, feijão, leite), com a quantidade de referência de cada uma.
- **`produto_extraido`** — produtos coletados via web scraping para cada categoria (nome, marca, preço unitário, URL de origem, data da coleta).

```bash
python database.py   # cria cesta_basica.db com as três tabelas acima
```

`cesta_basica.db` já está incluído neste repositório com o schema criado.
