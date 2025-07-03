<h1>Controle de Acesso - Condomínio 🏢🔐</h1>
<p>Este é um projeto desenvolvido em Python utilizando a biblioteca PySide6 (Qt para Python) que permite o gerenciamento de acessos em um condomínio, 
com funcionalidades como cadastro, edição, busca e exportação de visitantes.</p>

<h2>📌 Funcionalidades</h2>
✅ Cadastro de visitantes com:

- Nome
- CPF
- RG
- Empresa
- Responsável
- Data e Hora de registro automático

<h4>🔍 Busca rápida por CPF</h4>

<h4>📝 Edição de visitantes selecionados</h4>

<h4>❌ Exclusão de registros selecionados</h4>

<h4>📥 Importação de dados via Excel (em desenvolvimento)</h4>

<h4>📤 Exportação dos dados para Excel</h4>

<h4>📊 Visualização de todos os registros em tabela não editável</h4>

<h4>🖼️ Interface</h4>

<p>A interface é construída com QWidgets do PySide6 e possui:</p>
- Campos de formulário para entrada de dados
- Botões de ação (Adicionar, Editar, Excluir, Buscar)
- Tabela com 6 colunas (incluindo Data/Hora)
- Layouts organizados para fácil usabilidade

<h2>🛠️ Requisitos</h2>

- Python 3.8+
- PySide6
- Pandas (para importação/exportação de dados)

<h2>🧩 Estrutura de Código</h2>
<p>A lógica principal da interface está centralizada na classe AcessoView, que:</p>

- Define a janela principal e seus layouts
- Manipula os eventos de botão (adição, exclusão, busca)
- Gerencia a tabela com os registros
- Permite importação/exportação dos dados

<h2>📁 Possibilidades futuras</h2>
<p>Conexão com banco de dados (SQLite ou PostgreSQL)</p>

- Cadastro de moradores e associar visitantes a apartamentos
- Geração de relatórios automáticos

<h2>Integração com leitor facial ou QR Code🔳</h2>

🧑‍💻 Autor
Gustavo Vilela dos Santos<br>
<a href="https://www.linkedin.com/in/gustavo-vilela-46440b242/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
