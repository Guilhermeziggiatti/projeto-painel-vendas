# 🤖 Relatório Automatizado de Validação – Painel de Vendas

**Análise realizada por:** Script Python (`validar_painel.py`)  
**Data:** 26/07/2025  
**Arquivo analisado:** `painel.xlsx`

---

## ⚠️ Erros Detectados

### ❌ Erro na linha 6 – Coluna "Total"
- **Descrição:** O valor esperado era `R$ 4000.00`, mas foi encontrado `R$ -50,00 ❌`.
- **Impacto:** Pode gerar relatórios financeiros incorretos e decisões de negócio comprometidas.
- **Status:** Aguardando correção manual no Excel.

---

## ✔️ Observações
- Os dados foram validados automaticamente utilizando Pandas e OpenPyXL.
- Recomenda-se corrigir os valores com erro e rodar novamente o script para garantir a consistência.
