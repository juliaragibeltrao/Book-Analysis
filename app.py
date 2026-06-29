import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Book Analysis", layout="wide")
st.title("Análise de Preco Medio dos Livros")

df = pd.read_csv("BooksDatasetClean.csv")
df["Publish Date (Year)"] = pd.to_numeric(df["Publish Date (Year)"])
df["Price Starting With ($)"] = pd.to_numeric(df["Price Starting With ($)"], errors="coerce")

st.sidebar.header("Filtros")

ano_min = int(df["Publish Date (Year)"].min())
ano_max = int(df["Publish Date (Year)"].max())
anos = st.sidebar.slider("Intervalo de anos", ano_min, ano_max, (1970, 2023))

remover_outlier = st.sidebar.checkbox("Remover outlier (Smoky the Cowhorse, 1926)", value=True)

df_filtrado = df[(df["Publish Date (Year)"] >= anos[0]) & (df["Publish Date (Year)"] <= anos[1])]

if remover_outlier:
    df_filtrado = df_filtrado[
        ~((df_filtrado["Title"] == "Smoky the Cowhorse") & (df_filtrado["Publish Date (Year)"] == 1926))
    ]

preco_medio = df_filtrado.groupby("Publish Date (Year)")["Price Starting With ($)"].mean()
qtd_livros = df_filtrado.groupby("Publish Date (Year)").size()

col1, col2, col3 = st.columns(3)
col1.metric("Total de livros", len(df_filtrado))
col2.metric("Período", f"{anos[0]} - {anos[1]}")
col3.metric("Preço médio geral", f"${preco_medio.mean():.2f}")

tabs = st.tabs(["Preco medio por ano", "Quantidade de livros por ano"])

with tabs[0]:
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(preco_medio.index, preco_medio.values,
            color="#2E86AB", linewidth=2.5, marker="o", markersize=4)
    ax.fill_between(preco_medio.index, preco_medio.values,
                    alpha=0.15, color="#2E86AB")
    ax.set_title("Preço Médio por Ano", fontsize=16, fontweight="bold")
    ax.set_xlabel("Ano", fontsize=12)
    ax.set_ylabel("Preço Médio ($)", fontsize=12)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with tabs[1]:
    fig2, ax2 = plt.subplots(figsize=(14, 6))
    ax2.bar(qtd_livros.index, qtd_livros.values, color="#2E86AB", alpha=0.8)
    ax2.set_title("Quantidade de Livros por Ano", fontsize=16, fontweight="bold")
    ax2.set_xlabel("Ano", fontsize=12)
    ax2.set_ylabel("Quantidade", fontsize=12)
    ax2.grid(True, alpha=0.3, axis="y")
    st.pyplot(fig2)

with st.expander("Dados completos"):
    st.dataframe(df_filtrado.head(100), use_container_width=True)
