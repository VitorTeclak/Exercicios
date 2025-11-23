Este projeto está sendo totalmente feito por mim sozinho com base em que aprendi em cursos ou videos apenas para treinamento e exibir meus conhecimentos.

<h1>Documentação</h1>
Projeto Concessionária — Sistema CLI + API (Python)

Este projeto é um sistema completo para gerenciamento de uma concessionária, desenvolvido com foco em demonstrar habilidades práticas em Python, programação estruturada, modelagem de dados, MySQL, APIs REST com FastAPI, e organização de código em camadas.

O sistema funciona via CLI (linha de comando) e conta com uma API REST para operações como login e integração externa.

📌 Funcionalidades do Sistema
✅ Módulos principais (CLI)

Cadastro de veículos

Visualização de veículos

Remoção de veículos

Edição de veículos

Venda de veículos

Cadastro de clientes

Visualização de clientes

Edição de clientes

Exclusão de clientes

✅ API REST (FastAPI)

Atualmente implementado:

Login com senha hash (bcrypt)

Retorno do nível de acesso do funcionário

Endpoints localizados em:
backend/api/controllers.py

🛢 Banco de Dados (MySQL)

O banco segue um modelo simples, com tabelas como:

cliente

funcionario

veiculo

vendas

pessoa

Todas as tabelas e FKs estão definidas no arquivo:

📄 codigoMysql/codigo.sql

🔐 Autenticação (API)

A API usa bcrypt para armazenar senhas com segurança.

Fluxo do login:

Recebe JSON com login e senha

Busca o hash no banco

Usa bcrypt.checkpw() para validação

Retorna o nível de acesso do funcionário
