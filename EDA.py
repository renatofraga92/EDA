import pandas as pd
import numpy as np

# dataset fictício de vendas
np.random.seed(42)
dates = pd.date_range(start='2025-05-01', end='2025-05-31', freq='D')
products = ['T-Shirt', 'Pants', 'Shoes', 'Cap']
regions = ['SP', 'RJ', 'MG']

data = {
    'Date': dates,
    'Product': np.random.choice(products, size=len(dates)),
    'Quantity': np.random.randint(5, 20, size=len(dates)),
    'Unit Price': np.random.uniform(20, 150, size=len(dates)).round(2),
    'Region': np.random.choice(regions, size=len(dates))
}

df = pd.DataFrame(data)

# Total Sale e adicionar custo
df['Total Sale'] = df['Quantity'] * df['Unit Price']
df['Cost'] = df['Unit Price'] * 0.6  # Supondo que o custo é 60% do preço unitário
df['Profit'] = df['Total Sale'] - (df['Cost'] * df['Quantity'])

# Exibir as primeiras linhas
print(df.head(40))

#Manipulação de Dados com Pandas
#Vamos usar groupby(), merge(), e pivot_table() para explorar o dataset.

#groupby(): Agrupar e Agregar Dados
#média de Total Sale e Profit por Region e Product

# Agrupar por Region e Product
grouped = df.groupby(['Region', 'Product'])

# média de Total Sale e Profit
result = grouped[['Total Sale', 'Profit']].mean().round(2)
print(result)


freight_data = pd.DataFrame({
    'Region': ['SP', 'RJ', 'MG'],
    'Freight Cost': [5.0, 7.0, 6.0]
})

df = df.merge (freight_data, on='Region', how='left')
df['Freight'] = df['Quantity'] * df['Freight Cost']

#Ajuste do Profit considerando o custo de frete
df['Profit'] = df['Profit'] - df['Freight']*df['Quantity']

print("\nDataset após merge com Freight Cost:")
print(df[['Region', 'Quantity', 'Freight Cost', 'Profit']].head())

#pivot_table(): Resumir Dados
#tabela dinâmica para mostrar o Total Sale médio por Product e Region

# tabela dinâmica
pivot = pd.pivot_table(df, values='Total Sale', index='Product', columns='Region', aggfunc='mean').round(2)

print("\nTabela Dinâmica - Total Sale médio por Product e Region:")
print(pivot)

#Cálculos Numéricos com NumPy
#Vamos usar NumPy para calcular métricas financeiras, como médias e desvios padrão.

#Média e Desvio Padrão
#média e o desvio padrão de Unit Price, Total Sale e Profit

# média e desvio padrão
mean_price = np.mean(df['Unit Price'])
std_price = np.std(df['Unit Price'])

mean_sale = np.mean(df['Total Sale'])
std_sale = np.std(df['Total Sale'])

mean_profit = np.mean(df['Profit'])
std_profit = np.std(df['Profit'])

print("\nMédia e Desvio Padrão:")
print(f"Preço Unitário: Média = {mean_price:.2f}, Desvio Padrão = {std_price:.2f}")
print(f"Total Sale: Média = {mean_sale:.2f}, Desvio Padrão = {std_sale:.2f}")


#Margem de Lucro Média
#margem de lucro média (em %) usando NumPy

# margem de lucro média
mean_margin = np.mean(df['Profit'] / df['Total Sale']) * 100

print("\nMargem de Lucro Média:")
print(f"{mean_margin:.2f}%")


#Gráfico de Dispersão (Matplotlib)
#Visualize a relação entre Unit Price e Total Sale

import matplotlib.pyplot as plt

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Unit Price'], df['Total Sale'], color='blue', alpha=0.5)
plt.title('Relação entre Preço Unitário e Total Sale')
plt.xlabel('Preço Unitário')
plt.ylabel('Total Sale')
plt.grid(True)
plt.show()

#Histograma (Seaborn)
#Visualize a distribuição de Total Sale

import seaborn as sns

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['Total Sale'], kde=True, color='green')
plt.title('Distribuição de Total Sale')
plt.xlabel('Total Sale')
plt.ylabel('Contagem')
plt.grid(axis='y')
plt.show()

#Gráfico de Linhas (Plotly)
#Visualize a evolução de Total Sale ao longo do tempo

import plotly.express as px

# Gráfico de linhas
fig = px.line(df, x='Date', y='Total Sale', title='Evolução de Total Sale ao longo do tempo')
fig.show()

# Correlação de Pearson
#Calcule a correlação de Pearson entre Unit Price e Total Sale

# Calcular correlação de Pearson
correlation = df['Unit Price'].corr(df['Total Sale'])

#Gráfico de Dispersão com Hue (Seaborn)
#Adicione a dimensão de Product ao gráfico de dispersão

# Gráfico de dispersão com Hue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Unit Price', y='Total Sale', hue='Product', palette='viridis', size='Quantity')
plt.title('Relação entre Preço Unitário e Total Sale por Produto')
plt.xlabel('Preço Unitário')
plt.ylabel('Total Sale')
plt.grid(True)
plt.show()


#Produtos e regiões com maior lucro médio
print("\nProdutos e regiões com maior lucro médio:")
print(df.groupby(['Product', 'Region'])['Profit'].mean().idxmax())

#Como o custo de frete impacta o lucro
print("\nImpacto do custo de frete no lucro:")
print(df.groupby('Region')['Profit'].sum())

#Variabilidade do lucro por região
print("\nVariabilidade do lucro por região:")
print(df.groupby('Region')['Profit'].std())
#Boxplot do lucro por região
#Visualize a variabilidade do lucro por região usando um boxplot
print("\nBoxplot do lucro por região:")
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Region', y='Profit', palette='viridis')
plt.title('Variabilidade do Lucro por Região')
plt.ylabel('Lucro')
plt.grid(axis='y')
plt.show()

#Conclusão
#Neste projeto, exploramos um dataset fictício de vendas usando Pandas, NumPy e visualizações com Matplotlib, Seaborn e Plotly.
#Aprendemos como agrupar e agregar dados, criar tabelas dinâmicas, calcular métricas financeiras, visualizar dados e muito mais.
#Essas habilidades são essenciais para analisar e interpretar dados, bem como para tomar decisões baseadas em dados.
