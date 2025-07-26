# 🐞 Relatório de Defeitos – Painel de Vendas

**Análise realizada por:** Guilherme Ziggiatti  
**Data:** 26/07/2025  
**Sistema analisado:** painel.xlsx

---

## Erros encontrados:

### ❌ Erro 1 – Total incorreto (Linha 6)
- **Descrição**: O total da venda está como R$ 1500,00, porém o correto seria R$ 4000,00 × 1 = R$ 4000,00.
- **Impacto**: Pode gerar relatórios financeiros incorretos.
- **Status**: Aguardando correção.

---

### ❌ Erro 2 – Vendedor ausente (Linha 5)
- **Descrição**: A célula da coluna "Vendedor" está vazia.
- **Impacto**: Compromete rastreabilidade e análise de performance.
- **Status**: Em aberto.

---

### ❌ Erro 3 – Data inválida (Linha 4)
- **Descrição**: A data informada é de 2026, fora do intervalo esperado de análise.
- **Impacto**: Pode gerar distorções em relatórios temporais.
- **Status**: Em análise.

---

### ❌ Erro 4 – Total negativo e desconto > 100% (Linha 7)
- **Descrição**: Desconto de 120% resultou em valor total negativo (R$ -50,00).
- **Impacto**: Erro crítico que pode gerar problemas financeiros graves.
- **Status**: Crítico.

---

**Conclusão:**  
Foram encontrados **4 defeitos significativos** que comprometem a confiabilidade dos dados do painel. Recomenda-se revisão urgente das fórmulas e validações do sistema.
