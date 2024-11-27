create database sistema_de_vendas;

use sistema_de_vendas;

create table produtos(
	id int auto_increment primary key,
    nome varchar(50),
    desc_produto varchar(100),
    qnt_estoque int,
    valor decimal(10,2)
);

create table usuarios(
	id int auto_increment primary key,
    nome varchar(50),
    login varchar(50),
    senha varchar(50)
);

create table vendas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_nome VARCHAR(100),
    cliente_cpf VARCHAR(14),
    cliente_endereco VARCHAR(255),
    forma_pagamento VARCHAR(50),
    produto_id INT,
    quantidade INT,
    vendedor_id INT,
    valor_total DECIMAL(10, 2),
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
);