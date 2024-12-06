create database sistema_vendas_teste;

use sistema_vendas_teste;

CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255)
);

CREATE TABLE Produtos (
	id INT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(10, 2),
    estoque INT
);

CREATE TABLE Vendas (
    id INT PRIMARY KEY,
    clienteID INT,
    dataVenda DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (clienteID) REFERENCES Clientes(id)
);

CREATE TABLE ItensVenda (
    id INT PRIMARY KEY,
    vendaID INT,
    produtoID INT,
    quantidade INT,
    preco DECIMAL(10, 2),
    FOREIGN KEY (vendaID) REFERENCES Vendas(id),
    FOREIGN KEY (produtoID) REFERENCES Produtos(id)
);

DELIMITER $$

CREATE TRIGGER AtualizaEstoque
AFTER INSERT ON ItensVenda
FOR EACH ROW
BEGIN
    UPDATE Produtos
    SET estoque = estoque - NEW.quantidade
    WHERE id = NEW.produtoID;
END$$

DELIMITER ;

INSERT INTO Clientes (id, nome, endereco) VALUES
(1, 'Maria', 'Rua A, 123'),
(2, 'João', 'Avenida B, 456'),
(3, 'Ana', 'Praça C, 789');

INSERT INTO Produtos (id, nome, descricao, preco, estoque) VALUES
(1, 'Notebook', 'Notebook Dell', 3500.00, 10),
(2, 'Smartphone', 'Smartphone Samsung', 2500.00, 20),
(3, 'Tablet', 'Tablet com tela grande', 1500.00, 15);

INSERT INTO Vendas (id, clienteID, dataVenda, total) VALUES
(1, 1, '2024-12-05', 5000.00),
(2, 2, '2024-12-06', 2500.00);

INSERT INTO ItensVenda (id, vendaID, produtoID, quantidade,preco) VALUES
(1, 1, 1, 1, 3500.00),
(2, 1, 3, 1, 1500.00),
(3, 2, 2, 1, 2500.00);

SELECT * FROM Produtos;

SELECT V.id, V.dataVenda, V.total, C.nome, C.endereco, C.telefone
FROM Vendas V
JOIN clientes C ON V.clienteID = C.clienteID;





