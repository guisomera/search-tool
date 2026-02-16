# Busca de Arquivos – Contas a Pagar

Aplicação desktop desenvolvida em Python para localizar rapidamente palavras-chave dentro de arquivos de uma pasta específica.

A ferramenta foi criada para resolver um problema real do dia a dia financeiro: a necessidade de encontrar informações específicas dentro de múltiplos arquivos do banco, reduzindo tempo de busca manual e aumentando a produtividade.

---

## 🎯 Objetivo

Automatizar a busca de termos dentro de arquivos locais, oferecendo uma interface simples e eficiente para usuários não técnicos.

---

## 🧩 Funcionalidades

- Seleção de pasta no sistema
- Busca por palavra-chave dentro dos arquivos
- Exibição dos arquivos onde o termo foi encontrado
- Feedback visual de estados:
  - Mensagem inicial orientativa
  - Estado de carregamento
  - Resultado encontrado
  - Nenhum resultado
- Execução da busca pressionando **Enter**
- Interface gráfica amigável (Tkinter)
- Empacotamento como executável `.exe` para distribuição interna

---

## 🖥️ Interface

A aplicação possui uma interface simples e funcional:

- Botão para selecionar a pasta
- Campo para inserir palavra-chave
- Botão de busca
- Área de resultados com rolagem
- Mensagens centralizadas para estados do sistema

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter (interface gráfica)
- PyInstaller (empacotamento para Windows)

---

## 🚀 Como Executar (Modo Desenvolvimento)

1. Clone o repositório:

```bash
git clone https://github.com/guisomera/search-tool.git
cd search-tool
