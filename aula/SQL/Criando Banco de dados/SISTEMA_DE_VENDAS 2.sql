
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11) UNIQUE,
    endereco VARCHAR(255)
);

CREATE TABLE Funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(100),
    login VARCHAR(50) UNIQUE,
    senha VARCHAR(50)
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
    funcionarioID INT,
    dataVenda DATE,
    formaPagamento VARCHAR(50),
    parcelas INT,
    total DECIMAL(10, 2),
    FOREIGN KEY (clienteID) REFERENCES Clientes(id),
    FOREIGN KEY (funcionarioID) REFERENCES Funcionarios(id)
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


INSERT INTO Clientes (id, nome, cpf, endereco) VALUES
(1, 'Maria Silva', '12345678901', 'Rua A, 123'),
(2, 'João Santos', '23456789012', 'Avenida B, 456'),
(3, 'Ana Pereira', '34567890123', 'Praça C, 789');

INSERT INTO Funcionarios (id, nome, cargo, login, senha) VALUES
(1, 'Carlos Lima', 'Vendedor', 'carlos', 'senha123'),
(2, 'Fernanda Souza', 'Administrador', 'fernanda', 'senha456'),
(3, 'Lucas Almeida', 'Vendedor', 'lucas', 'senha789');

INSERT INTO Produtos (id, nome, descricao, preco, estoque) VALUES
(1, 'Notebook', 'Notebook Dell', 3500.00, 10),
(2, 'Smartphone', 'Smartphone Samsung', 2500.00, 20),
(3, 'Tablet', 'Tablet com tela grande', 1500.00, 15);


INSERT INTO Vendas (id, clienteID, funcionarioID, dataVenda, formaPagamento, parcelas, total) VALUES
(1, 1, 1, '2024-12-05', 'à vista', 1, 5000.00),
(2, 2, 2, '2024-12-06', 'parcelado', 3, 2500.00);

INSERT INTO ItensVenda (id, vendaID, produtoID, quantidade, preco) VALUES
(1, 1, 1, 1, 3500.00),
(2, 1, 3, 1, 1500.00),
(3, 2, 2, 1, 2500.00);

SELECT
    C.nome AS NomeCliente,
    F.nome AS NomeVendedor,
    P.nome AS ProdutoComprado,
    I.preco * I.quantidade AS ValorTransacao,
    V.dataVenda
FROM Vendas V
JOIN Clientes C ON V.clienteID = C.id
JOIN Funcionarios F ON V.funcionarioID = F.id
JOIN ItensVenda I ON V.id = I.vendaID
JOIN Produtos P ON I.produtoID = P.id;


