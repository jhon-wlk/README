import pandas as pd

# Lendo o arquivo CSV
data = pd.read_csv("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_NEW_4_sprint/vehicles.csv")

# Exibindo as primeiras linhas para verificar se carregou corretamente
print(data.head())

