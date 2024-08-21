import pandas as pd
import numpy as np

# Configuração para reprodutibilidade
np.random.seed(42)

# Gerando datas
dates = pd.date_range(start="2023-01-01", periods=365, freq="D")

# Gerando preços fictícios para uma ação
prices = np.random.normal(loc=100, scale=10, size=len(dates)).cumsum()  # Preços acumulados para simular tendência

# Criando um DataFrame
data = pd.DataFrame(data={'Date': dates, 'Price': prices})
data.set_index('Date', inplace=True)

# Exibindo os primeiros registros
print(data.head())

# Limpeza de Dados (removendo possíveis valores negativos)
data['Price'] = data['Price'].apply(lambda x: max(x, 0))

# Cálculo da Média Móvel de 7 dias
data['7-day MA'] = data['Price'].rolling(window=7).mean()

# Cálculo da Variação Diária em Percentual
data['Daily Change %'] = data['Price'].pct_change() * 100

# Exibindo as primeiras entradas após a manipulação
print(data.head(10))

import matplotlib.pyplot as plt

# Plotando a série temporal do preço da ação
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Price'], label='Preço')
plt.plot(data.index, data['7-day MA'], label='Média Móvel de 7 dias', linestyle='--')
plt.title('Preço da Ação ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.show()

# Plotando a variação diária percentual
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Daily Change %'], color='orange', label='Variação Diária %')
plt.title('Variação Diária Percentual do Preço da Ação')
plt.xlabel('Data')
plt.ylabel('Variação %')
plt.legend()
plt.grid(True)
plt.show()

# Plotando médias mensais
monthly_data = data['Price'].resample('M').mean()

plt.figure(figsize=(12, 6))
plt.bar(monthly_data.index, monthly_data, color='purple')
plt.title('Média Mensal do Preço da Ação')
plt.xlabel('Mês')
plt.ylabel('Preço Médio')
plt.grid(True)
plt.show()

# Resumindo insights
monthly_summary = data.resample('M').agg({
    'Price': ['mean', 'min', 'max'],
    'Daily Change %': ['mean']
})

print(monthly_summary)