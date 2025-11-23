CREATE DATABASE concessionaria;
USE concessionaria;

CREATE TABLE endereco (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(100) NOT NULL,
    numero INT NOT NULL,
    cep VARCHAR(8) NOT NULL,
    bairro VARCHAR(100),
    complemento VARCHAR(100)
);

CREATE TABLE pessoa (
    id_pessoa INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    idade INT,
    telefone VARCHAR(11),
    email VARCHAR(100),
    id_endereco INT NOT NULL,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    id_pessoa INT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa)
);

CREATE TABLE funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    id_pessoa INT NOT NULL,
    cargo ENUM('Vendedor','Supervisor_de_vendas','Gerente','RH') NOT NULL,
    nivel_acesso  NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa)
);

CREATE TABLE veiculo (
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    modelo_veiculo VARCHAR(100) NOT NULL,
    cor VARCHAR(50) NOT NULL,
    ano_producao INT NOT NULL,
    quilometragem VARCHAR(15),
    placa VARCHAR(7) UNIQUE NOT NULL,
    valor VARCHAR(15) NOT NULL,
    tipo ENUM('CARRO', 'MOTO') NOT NULL
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_funcionario INT NOT NULL,
    id_veiculo INT NOT NULL,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario),
    FOREIGN KEY (id_veiculo) REFERENCES veiculo(id_veiculo)
);
