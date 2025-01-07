import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
data = pd.read_csv("C:\\Users\\Jhonw\\OneDrive\\Documents\\GitHub\\README\\vehicles_new.csv)  # Substitua com o caminho correto

# Exibir as colunas do DataFrame para o usuário
st.header("Escolha as colunas para os gráficos")

# Selecionar coluna para o histograma
hist_column = st.selectbox("Selecione a coluna para o histograma", data.columns)

# Selecionar colunas para o gráfico de dispersão
scatter_x = st.selectbox("Selecione a coluna para o eixo X do gráfico de dispersão", data.columns)
scatter_y = st.selectbox("Selecione a coluna para o eixo Y do gráfico de dispersão", data.columns)

# Botão para criar histograma
if st.button('Criar histograma'):
    st.write(f"Criando um histograma para a coluna '{hist_column}'")
    fig_hist = px.histogram(data, x=hist_column)
    st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar gráfico de dispersão
if st.button('Criar gráfico de dispersão'):
    st.write(f"Criando um gráfico de dispersão para as colunas '{scatter_x}' e '{scatter_y}'")
    fig_scatter = px.scatter(data, x=scatter_x, y=scatter_y)
    st.plotly_chart(fig_scatter, use_container_width=True)




