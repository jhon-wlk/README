import pandas as pd

# Lendo o arquivo CSV
data = pd.read_csv("vehicles_new.csv")
data = pd.read_csv("C:/Users/Jhonw/OneDrive/Documents/GitHub/README/vehicles_new.csv")

# Exibindo as primeiras linhas para verificar se carregou corretamente
print(data.head())

