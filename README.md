# Book Analysis

Análise exploratória de um dataset de livros, focada na evolução do **preço médio por ano**.

## Dataset

`BooksDatasetClean.csv` — contém dados de **103.063 livros** com as seguintes colunas:
Título, Autores, Descrição, Categoria, Editora, Preço, Mês e Ano de publicação.

## Perguntas exploradas

1. **Quantos livros existem por mês/ano?**
   - Agrupamento inicial para conhecer a distribuição dos dados.
2. **Há anos faltantes após 1900?**
   - Não — todos os anos de 1900 a 2023 possuem ao menos um livro registrado.
3. **O preço médio cresce com o tempo ou se mantém estável?**
   - Análise do preço médio anual de 1970 a 2023, com remoção de outlier identificado.
4. **Há outliers?**
   - Sim: *"Smoky the Cowhorse"* (1926, US\$ 879,50) — valor muito acima dos demais, distorcendo a média. Removido da análise.

## Notebook

`analise_precos.ipynb` — contém todo o fluxo:
1. Carregamento e tratamento dos dados
2. Remoção de outliers
3. Agrupamento por ano e cálculo do preço médio
4. Visualização com matplotlib

## Como usar

```bash
pip install pandas matplotlib jupyter
python -m notebook
```

Abra o arquivo `analise_precos.ipynb` e execute as células sequencialmente.
