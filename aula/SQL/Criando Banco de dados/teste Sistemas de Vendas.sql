CREATE DATABASE sistema_de_vendas;

USE sistema_de_vendas;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    qnt_estoque INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    cliente_cpf VARCHAR(14) NOT NULL,
    cliente_endereco VARCHAR(255) NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    vendedor_id INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
);

INSERT INTO produtos (nome, descricao, qnt_estoque, valor) VALUES
('Caneta Azul', 'Caneta esferográfica azul', 100, 2.50),
('Caderno A4', 'Caderno 200 folhas', 50, 15.00),
('Borracha', 'Borracha branca escolar', 200, 1.00),
('Lápis Preto', 'Lápis preto nº 2', 150, 1.50);

INSERT INTO usuarios (nome, senha) VALUES
('Ana Vendedora', 'senha123'),
('Carlos ADM', 'adm456'),
('Mariana Vendedora', 'mariana789');

INSERT INTO vendas (cliente_nome, cliente_cpf, cliente_endereco, forma_pagamento, produto_id, quantidade, vendedor_id, valor_total) VALUES
('João Silva', '123.456.789-00', 'Rua das Flores, 123', 'Cartão de Crédito', 1, 10, 1, 25.00),
('Maria Souza', '987.654.321-00', 'Av. Central, 456', 'Dinheiro', 2, 5, 2, 75.00),
('Pedro Oliveira', '456.789.123-00', 'Rua dos Pinheiros, 789', 'Pix', 3, 20, 3, 20.00),
('Carla Mendes', '321.654.987-00', 'Av. das Palmeiras, 321', 'Boleto', 4, 15, 1, 22.50);


SELECT 
vendas.id AS venda_id, vendas.cliente_nome, vendas.cliente_cpf, produtos.nome AS produto_nome, forma_pagamento, vendas.quantidade, vendas.valor_total, usuarios.nome AS vendedor_nome, vendas.data_venda	
FROM vendas
INNER JOIN produtos ON vendas.produto_id = produtos.id
INNER JOIN usuarios ON vendas.vendedor_id = usuarios.id
ORDER BY vendas.data_venda DESC;






