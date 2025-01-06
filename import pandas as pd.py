import pandas as pd

# Lendo o arquivo CSV
data = pd.read_csv('vehicles_us.csv')

# Exibindo as primeiras linhas para verificar se carregou corretamente
print(data.head())

