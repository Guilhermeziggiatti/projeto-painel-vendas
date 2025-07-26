import pandas as pd

# Carregar a planilha
arquivo = "painel.xlsx"
df = pd.read_excel(arquivo)

erros = []

# 🔍 Teste 1 – Validar o total da venda na linha 6
linha_erro = 5  # Linha 6 na planilha (index 5 no Python)
total_venda = df.loc[linha_erro, "Total"]
valor_esperado = 4000.00

if total_venda != valor_esperado:
    erros.append(f"Erro no total da linha 6: esperado R$ {valor_esperado}, encontrado R$ {total_venda}")

# 🔍 Teste 2 – Verificar vendedor ausente na linha 5
linha_verificar = 4  # Linha 5 na planilha
vendedor = df.loc[linha_verificar, "Vendedor"]

if pd.isna(vendedor) or vendedor == "":
    erros.append("Erro: Vendedor ausente na linha 5.")

# 📋 Resultado
if erros:
    print("🚨 Erros encontrados:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("✅ Nenhum erro encontrado.")
