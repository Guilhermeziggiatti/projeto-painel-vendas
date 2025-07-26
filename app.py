import streamlit as st
import pandas as pd

st.set_page_config(page_title="Validador de Planilha de Vendas", layout="wide")

st.title("🔍 Validador de Planilha de Vendas")

st.markdown("📂 Faça upload da planilha de vendas (.xlsx)")

arquivo = st.file_uploader("Arraste e solte o arquivo aqui", type=["xlsx"])

def validar_total(row):
    try:
        preco = float(str(row['Preço Unitário']).replace('R$', '').replace(',', '.').strip())
        quantidade = int(row['Qtd'])
        total_esperado = round(preco * quantidade, 2)

        total_informado = float(str(row['Total']).replace('R$', '').replace(',', '.').strip())
        if abs(total_esperado - total_informado) > 0.01:
            return f"Total incorreto: Esperado R$ {total_esperado:.2f}, Encontrado R$ {total_informado:.2f}"
    except Exception as e:
        return f"Erro na linha: {e}"
    return None

def validar_planilha(df):
    erros = []
    for idx, linha in df.iterrows():
        erro = validar_total(linha)
        if erro:
            erros.append((idx, erro))
    return erros

def carregar_planilha(arquivo):
    try:
        df = pd.read_excel(arquivo)
        colunas_necessarias = ['Qtd', 'Preço Unitário', 'Total']
        for coluna in colunas_necessarias:
            if coluna not in df.columns:
                return None, [f"A planilha está faltando as colunas necessárias (esperado: 'Preço Unitário', 'Qtd', 'Total')"]
        return df, []
    except Exception as e:
        return None, [f"Erro ao ler o arquivo: {e}"]

if arquivo:
    df, erros_estrutura = carregar_planilha(arquivo)

    if erros_estrutura:
        st.error(erros_estrutura[0])
    else:
        st.subheader("📊 Pré-visualização da Planilha")
        st.dataframe(df)

        if st.button("🔍 Validar"):
            erros = validar_planilha(df)

            if not erros:
                st.success("✅ Todos os valores estão corretos!")
            else:
                st.error("❌ Erros encontrados na planilha:")
                for idx, erro in erros:
                    st.markdown(f"- Linha {idx + 2}: {erro}")
