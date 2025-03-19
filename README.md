# Análise Exploratória de Dados (EDA)
# Projeto de Análise de Dados de Vendas

## Visão Geral
Este projeto realiza uma análise exploratória de dados (EDA) em um conjunto de dados fictício de vendas usando Python. Ele utiliza bibliotecas como Pandas, NumPy, Matplotlib, Seaborn e Plotly para manipular dados, calcular métricas financeiras e gerar visualizações. O objetivo é descobrir insights sobre o desempenho de vendas, lucratividade e variações regionais, que podem informar estratégias de precificação e decisões de negócios.

## Funcionalidades
- **Manipulação de Dados com Pandas**:
  - Usa `groupby()` para agregar dados por `Region` e `Product`.
  - Aplica `merge()` para integrar dados de custo de frete e ajustar os cálculos de lucro.
  - Cria uma `pivot_table()` para resumir a média de `Total Sale` por `Product` e `Region`.
- **Cálculos Numéricos com NumPy**:
  - Calcula média e desvio padrão para `Unit Price`, `Total Sale` e `Profit`.
  - Calcula a margem de lucro média.
- **Visualizações**:
  - Gráfico de dispersão (Matplotlib) para explorar a relação entre `Unit Price` e `Total Sale`.
  - Histograma (Seaborn) para visualizar a distribuição de `Total Sale`.
  - Gráfico de linhas (Plotly) para mostrar a evolução de `Total Sale` ao longo do tempo.
  - Gráfico de dispersão com hue (Seaborn) para analisar `Unit Price` vs `Total Sale` por `Product`.
  - Boxplot (Seaborn) para examinar a variabilidade de `Profit` por `Region`.
- **Insights**:
  - Identifica produtos e regiões com maior lucro médio.
  - Avalia o impacto dos custos de frete no lucro.
  - Analisa a variabilidade do lucro entre regiões.

## Dados
O projeto utiliza um conjunto de dados fictício de vendas para maio de 2025, com as seguintes colunas:
- `Date`: Data da venda (de 1 a 31 de maio de 2025).
- `Product`: Produto vendido (`T-Shirt`, `Pants`, `Shoes`, `Cap`).
- `Quantity`: Quantidade de unidades vendidas.
- `Unit Price`: Preço por unidade (em USD).
- `Region`: Região da venda (`SP`, `RJ`, `MG`).
- `Total Sale`: Receita total da venda (`Quantity` * `Unit Price`).
- `Cost`: Custo por unidade (assumido como 60% do `Unit Price`).
- `Profit`: Lucro após considerar custos e frete (`Total Sale` - (`Cost` * `Quantity`) - (`Freight` * `Quantity`)).
- `Freight Cost`: Custo de frete por unidade por região.
- `Freight`: Custo total de frete (`Quantity` * `Freight Cost`).

## Requisitos
- Python 3.x
- Bibliotecas necessárias: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
  - Instale com: `pip install pandas numpy matplotlib seaborn plotly`

## Etapas da Análise
1. **Criação dos Dados**:
   - Gera um conjunto de dados fictício de vendas para maio de 2025 com colunas como `Date`, `Product`, `Quantity`, `Unit Price`, `Region`, `Total Sale`, `Cost` e `Profit`.
2. **Manipulação de Dados com Pandas**:
   - Agrupa os dados por `Region` e `Product` para calcular a média de `Total Sale` e `Profit`.
   - Faz o merge com dados de custo de frete e ajusta o `Profit` de acordo.
   - Cria uma tabela dinâmica para resumir a média de `Total Sale` por `Product` e `Region`.
3. **Cálculos Numéricos com NumPy**:
   - Calcula média e desvio padrão para `Unit Price`, `Total Sale` e `Profit`.
   - Calcula a margem de lucro média.
4. **Visualizações**:
   - Gráfico de dispersão para explorar a relação entre `Unit Price` e `Total Sale`.
   - Histograma para visualizar a distribuição de `Total Sale`.
   - Gráfico de linhas para mostrar `Total Sale` ao longo do tempo.
   - Gráfico de dispersão com hue para analisar `Unit Price` vs `Total Sale` por `Product`.
   - Boxplot para examinar a variabilidade de `Profit` por `Region`.
5. **Insights**:
   - Identifica o produto e a região com maior lucro médio.
   - Avalia o impacto dos custos de frete no lucro por região.
   - Analisa a variabilidade do lucro entre regiões usando desvio padrão e boxplots.

## Observações e Insights
- **Maior Lucro Médio**: A combinação de produto e região com maior lucro médio é identificada (ex.: `Shoes` em `SP`).
- **Impacto do Custo de Frete**: Regiões com custos de frete mais altos (ex.: `RJ` com $7.0 por unidade) mostram uma redução significativa no lucro, sugerindo a necessidade de otimizar a logística.
- **Variabilidade do Lucro**: O boxplot e o desvio padrão revelam quais regiões têm maior variabilidade no lucro, indicando possíveis inconsistências em vendas ou custos.
- **Correlação**: A correlação de Pearson entre `Unit Price` e `Total Sale` ajuda a entender o impacto do preço na receita.
- **Distribuição**: O histograma de `Total Sale` mostra a distribuição dos valores de vendas, útil para identificar faixas de receita comuns.

## Conclusão
Este projeto demonstra habilidades essenciais de análise de dados usando Pandas, NumPy, Matplotlib, Seaborn e Plotly. Ele fornece uma base para analisar dados de vendas, calcular métricas financeiras e visualizar tendências, que são cruciais para tomar decisões baseadas em dados em áreas como precificação, logística e estratégias de vendas regionais.

## Licença
Este conteúdo, incluindo o script, a documentação e as visualizações geradas, é propriedade intelectual de seu criador. O uso, reprodução ou distribuição não autorizados deste conteúdo sem permissão prévia por escrito são estritamente proibidos. Por favor, entre em contato com renatofraga.rr@gmail.com para solicitações.