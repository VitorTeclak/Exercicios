Este projeto está sendo totalmente feito por mim sozinho com base em que aprendi em cursos ou videos apenas para treinamento e exibir meus conhecimentos.

<h1>Documentação</h1>
Projeto Concessionária — Sistema CLI + API (Python)

Este projeto é um sistema completo para gerenciamento de uma concessionária, desenvolvido com foco em demonstrar habilidades práticas em Python, programação estruturada, modelagem de dados, MySQL, APIs REST com FastAPI, e organização de código em camadas.

O sistema funciona via CLI (linha de comando) e conta com uma API REST para operações como login e integração externa.

📌 Funcionalidades do Sistema
✅ Módulos principais (CLI)
<ul>
<li>Cadastro de veículos</li>

<li>Visualização de veículos</li>

<li>Remoção de veículos</li>

<li>Edição de veículos</li>

<li>Venda de veículos</li>

<li>Cadastro de clientes</li>

<li>Visualização de clientes</li>

<li>Edição de clientes</li>

<li>Exclusão de clientes</li>
</ul>
✅ API REST (FastAPI)
<ul>
<li>Atualmente implementado:</li>

<li>Login com senha hash (bcrypt)</li>

<li>Retorno do nível de acesso do funcionário</li>

<li>Endpoints localizados em:
backend/api/controllers.py</li>
</ul>
<p>🛢 Banco de Dados (MySQL)</p>

<p>O banco segue um modelo simples, com tabelas como:</p>

<li>cliente</li>

<li>funcionario</li>

<li>veiculo</li>

<li>vendas</li>

<li>pessoa</li>

<p>Todas as tabelas e FKs estão definidas no arquivo:</p>

📄 codigoMysql/codigo.sql

🔐 Autenticação (API)

A API usa bcrypt para armazenar senhas com segurança.

Fluxo do login:

Recebe JSON com login e senha

Busca o hash no banco

Usa bcrypt.checkpw() para validação

Retorna o nível de acesso do funcionário

<h4>Design da Arquitetura</h4>
<p>Camada CLI<>/p
<ul>
<li>Implementa o menu principal (main.py)</li>

<li>Realiza solicitações ao usuário</li>

<li>Faz leitura e escrita no banco via SQLAlchemy</li>

<li>Para login, comunica-se com a API REST usando requests</li>
</ul>
<h4>Camada de Entidades</h4>
Localizada em /entities/
Define modelos lógicos que representam os objetos do sistema, como:
🧩 cliente.py
Armazena dados básicos do cliente utilizados durante operações de CRUD.
🚗 veiculo.py
Representa um veículo cadastrado no sistema.
Essas classes oferecem apenas a estrutura e identidade dos objetos — operações pesadas são feitas diretamente nas funções do CLI.
<h4>Camada de API (FastAPI)</h4>
Local: /backend/api/controllers.py
A API contém:
🔐 Endpoint de Login
<ul>
<li>Recebe login e senha via JSON</li>

<li>Busca o hash do usuário no banco</li>

<li>Usa bcrypt.checkpw() para validar</li>

<li>Retorna:</li>
<ul>
<li>nível de acesso (int) em caso de sucesso</li>

<li>erro em caso de falha</li>
</ul>
</ul>
<h4>Dependências</h4>
CLI:
<ul>
<li>pymysql</li>

<li>requests</li>

<li>dotenv</li>

<li>bcrypt</li>

<li>SQLAlchemy</li>
</ul>

API:
<ul>
<li>fastapi</li>

<li>uvicorn</li>

<li>sqlalchemy</li>

<li>bcrypt</li>
