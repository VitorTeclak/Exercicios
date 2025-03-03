Este projeto está sendo totalmente feito por mim sozinho com base em que aprendi em cursos ou videos apenas para treinamento e exibir meus conhecimentos.

<h1>Documentação</h1>
Após uma analíse simples foi verificado a necessidade de algumas coisas para realizar este sistema

<ul>
<li>Entrada de veiculos.</li>
<li>Visualizar estoque de Veiculos.</li>
<li>Excluir Veiculo.</li>
<li>Vender Veiculo.</li>
<li>Editar Veiculos.</li>
<li>Separar os carros e motos dos Veiculos.</li>
<li>Adicionar Clientes.</li>
<li>Visualizar lista de Clientes.</li>
<li>Editar dados de Clientes.</li>
<li>Excluir clientes da lista.</li>
<li>Vincular carros vendidos ao ID do Cliente comprador.</li>
</ul>

<h2>Explicação de funções</h2>
<h3>CLASSE MAIN</h3>
A Classe MAIN serve apenas para comportar e separar a o painel de controle das demais classes e funções.

<h3>CLASSE VEICULO</h3>
A classe veiculo foi criada para conter os principais dados de um veiculo para conseguir realizar a venda, dentre esses dados foi incluido dados como ("modelo, cor, ano de produção, quilometragem, valor, placa e tipo"), Sendo a coluna "TIPO" servindo unicamente para separar os veiculos carro e motos.
Dentro da classe Veiculo foram criadas as seguintes funções. 
<ul>
<li>Entrada de veiculos.</li>
<li>Visualizar estoque de Veiculos.</li>
<li>Excluir Veiculo.</li>
<li>Vender Veiculo.</li>
<li>Editar Veiculos.</li>
</ul>

<h3>CLASSE CLIENTE</h3>
A classe Cliente foi criada para conter os principais dados de um cliente como ("nome, telefone, email, cpf, idade e endereço") para armazenas os dados do endereço foi criada uma sub-classe sendo ativada automaticamente assim que inicia a criação da classe cliente.
Dentro da classe Cliente foram criadas as seguintes funções.
<ul>
<li>Adicionar Clientes.</li>
<li>Editar dados de Clientes.</li>
<li>Excluir clientes da lista.</li>
<li>Vincular carros vendidos ao ID do Cliente comprador.</li>
<li>Subclasse "Endereço" .</li>
</ul>
