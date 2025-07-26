# ✅ Projeto de QA – Validação de Painel de Vendas com Streamlit

Este projeto simula o trabalho de um Analista de Testes que valida a integridade de dados de vendas em uma planilha, identificando erros manuais e inconsistências comuns. A interface interativa foi construída com **Streamlit**, permitindo testes visuais e feedback em tempo real.

---

## 🎯 Objetivos do Projeto

- Detectar erros de cálculo no campo **Total** da planilha.
- Validar preenchimento correto de colunas como **Preço**, **Quantidade**, **Descontos (%)** e **Datas**.
- Oferecer uma ferramenta acessível e visual para análise de planilhas de vendas.
- Demonstrar aplicação prática de **Testes de QA** com apoio de automação.

---

## 🧪 Tipos de Teste Aplicados

- ✅ **Teste de valores calculados**: Confere se o Total = Preço × Quantidade.
- ❌ **Detecção de preenchimento incorreto**: Erros de digitação, formatos monetários inválidos etc.
- 🧠 **Validação de regras de negócio**: Descontos absurdos, valores negativos, campos vazios.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (pandas, openpyxl, streamlit)
- **Streamlit** para a interface visual dos testes
- **Excel (.xlsx)** como base de dados simulada
- **Git + GitHub** para versionamento

---

## 🖥️ Interface Visual

O projeto inclui um painel interativo que:

- Carrega uma planilha `.xlsx` via upload
- Mostra uma prévia dos dados
- Realiza validações automáticas com destaque visual dos erros
- Exibe relatórios técnicos no próprio navegador

---

## 📁 Estrutura do Projeto


---

## 👤 Autor

**Guilherme Ziggiatti**  
Último semestre de Administração no Mackenzie  
Estudante de QA com foco em testes manuais e automatizados  
GitHub: [@guilhermeziggiatti](https://github.com/guilhermeziggiatti)

---

## 🚀 Próximos Passos (Opcional)

- Exportar relatório final em PDF
- Implementar testes automatizados com `pytest`
- Adicionar upload em lote de múltiplas planilhas

