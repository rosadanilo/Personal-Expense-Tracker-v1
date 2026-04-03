# Personal-Expense-Tracker-v1
Este é um rastreador de despesas pessoais baseado em linha de comando (CLI) desenvolvido em Python. O projeto permite que o usuário gerencie suas finanças diárias, oferecendo funcionalidades de adição, visualização, soma total e agrupamento por categorias, com persistência de dados em arquivos locais.

🚀 Funcionalidades
Adição de Despesas: Registro de categoria, valor e observações opcionais.
Visualização em Tabela: Exibição limpa e organizada dos dados utilizando a biblioteca tabulate.
Persistência de Dados: Salvamento automático em formato JSON, garantindo que os dados não sejam perdidos ao fechar o programa.
Relatórios Rápidos: Visualização do gasto total e resumo de gastos agrupados por categoria.
Tratamento de Erros: Validação de entradas para evitar falhas por dados inválidos.

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem principal.
JSON: Formato para armazenamento de dados.
Tabulate: Biblioteca para formatação de tabelas no terminal.
OS & Path: Manipulação de caminhos de arquivos de forma segura.

📦 Como Instalar e Rodar
Clone o repositório:

Bash
git clone [https://github.com/seu-usuario/personal-expense-tracker.git
Acesse a pasta do projeto:
Bash
cd personal-expense-tracker

Instale as dependências:
Bash
pip install tabulate

Execute o programa:
Bash
python main.py

📂 Estrutura de Arquivos
main.py: Código fonte principal do aplicativo.
expenses.json: Arquivo gerado automaticamente para armazenar os dados.

README.md: Documentação do projeto.
