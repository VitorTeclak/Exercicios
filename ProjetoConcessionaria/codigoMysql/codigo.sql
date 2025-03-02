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

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    idade INT NOT NULL,
    telefone VARCHAR(11),
    email VARCHAR(100),
    id_endereco INT NOT NULL,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE veiculo (
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    modelo_veiculo VARCHAR(100) NOT NULL,
    cor VARCHAR(50) NOT NULL,
    ano_producao INT NOT NULL,
    quilometragem VARCHAR(15),
    placa VARCHAR(7) UNIQUE NOT NULL,
    valor VARCHAR(15) NOT NULL,
    tipo ENUM('CARRO', 'MOTO') NOT NULL,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);