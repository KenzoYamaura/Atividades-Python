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
    senha VARCHAR(50) NOT NULL,
    cargo VARCHAR(100) NOT NULL    
);

CREATE TABLE carrinho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    vendedor_id INT NOT NULL,
    quantidade INT NOT NULL,
    data_adicao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
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
('Caneta', 'Caneta azul', 100, 2.50),
('Caderno', 'Caderno 200 folhas A4', 50, 15.00),
('Borracha', 'Borracha branca', 200, 1.00),
('Lápis Preto', 'Lápis Nº2', 150, 1.50);

INSERT INTO usuarios (nome, senha, cargo) VALUES
('Ana', 112233, 'Vendedora'),
('Carlos', 332211, 'ADM'),
('Mariana', '223311', 'Vendedora'),
('Arthur', '4433', 'Vendedora');

INSERT INTO vendas (cliente_nome, cliente_cpf, cliente_endereco, forma_pagamento, produto_id, quantidade, vendedor_id, valor_total) VALUES
('João Silva', '123.456.789-00', 'Rua das Flores, 123', 'Cartão de Crédito', 1, 10, 1, 25.00),
('Maria Souza', '987.654.321-00', 'Av. Central, 456', 'Dinheiro', 2, 5, 2, 75.00),
('Pedro Oliveira', '456.789.123-00', 'Rua dos Pinheiros, 789', 'Pix', 3, 20, 3, 20.00),
('Carla Mendes', '321.654.987-00', 'Av. das Palmeiras, 321', 'Boleto', 4, 15, 1, 22.50);


-- Trigger para converter carrinho em venda automaticamente ao finalizar a compra
DELIMITER $$

CREATE TRIGGER finalizar_venda
AFTER INSERT ON carrinho
FOR EACH ROW
BEGIN
    INSERT INTO vendas (cliente_nome, cliente_cpf, cliente_endereco, forma_pagamento, produto_id, quantidade, vendedor_id, valor_total)
    VALUES (
        'Cliente Padrão',
        '000.000.000-00',
        'Endereço padrão',
        'Pagamento padrão',
        NEW.produto_id,
        NEW.quantidade,
        NEW.vendedor_id,
        (SELECT valor * NEW.quantidade FROM produtos WHERE id = NEW.produto_id)
    );
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER atualizar_estoque
AFTER INSERT ON vendas
FOR EACH ROW
BEGIN
    UPDATE produtos
    SET qnt_estoque = qnt_estoque - NEW.quantidade
    WHERE id = NEW.produto_id;
END$$

DELIMITER ;

SELECT 
    carrinho.id, 
    produtos.nome AS produto_nome,
    produtos.valor, 
    carrinho.quantidade, 
    (produtos.valor * carrinho.quantidade) AS total_parcial,
    usuarios.nome AS vendedor_nome,
    carrinho.data_adicao
FROM carrinho
INNER JOIN produtos ON carrinho.produto_id = produtos.id
INNER JOIN usuarios ON carrinho.vendedor_id = usuarios.id
ORDER BY carrinho.data_adicao DESC;


SELECT 
	vendas.cliente_nome, 
	usuarios.nome AS vendedor_nome, 
	produtos.nome AS produto_nome, 
	forma_pagamento, 
	vendas.quantidade, 
	vendas.valor_total, 
	vendas.data_venda	
FROM vendas
INNER JOIN produtos ON vendas.produto_id = produtos.id
INNER JOIN usuarios ON vendas.vendedor_id = usuarios.id
ORDER BY vendas.data_venda DESC; 

INSERT INTO carrinho (produto_id, vendedor_id, quantidade) VALUES
(1, 1, 5),
(2, 3, 2);

INSERT INTO carrinho (produto_id, vendedor_id, quantidade)
VALUES (1, 1, 2);




