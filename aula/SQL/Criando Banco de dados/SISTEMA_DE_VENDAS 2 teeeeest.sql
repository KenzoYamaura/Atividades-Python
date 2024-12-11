create database Sistemas_vendas;

use Sistemas_vendas;

create table clientes (
    id int primary key,
    nome varchar(100),
    cpf varchar(11),
    endereco varchar(255)
);

create table funcionarios (
    id int primary key,
    nome varchar(100),
    cargo varchar(100),
    login varchar(50),
    senha varchar(50)
);

create table produtos (
    id int primary key,
    nome varchar(100),
    descricao text,
    preco decimal(10, 2),
    estoque int
);

create table vendas (
    id int primary key,
    clienteID int,
    funcionarioID int,
    dataVenda datetime default current_timestamp,
    formaPagamento varchar(50),
    parcelas int,
    total decimal(10, 2),
    foreign key (clienteID) references clientes(id),
    foreign key (funcionarioID) references funcionarios(id)
);

CREATE TABLE itensVenda (
    id int primary key,
    vendaID int,
    produtoID int,
    quantidade int,
    preco decimal(10, 2),
    foreign key (vendaID) references vendas(id),
    foreign key (produtoID) references produtos(id)
);

DELIMITER $$

create trigger AtualizaEstoque
after insert on itensVenda
for each row
begin
    update produtos
    set estoque = estoque - new.quantidade
    where id = new.produtoID;
end$$

DELIMITER ;


insert into clientes (id, nome, cpf, endereco) values
(1, 'Maria Silva', '12345678901', 'Rua A, 123'),
(2, 'João Santos', '23456789012', 'Avenida B, 456'),
(3, 'Ana Pereira', '34567890123', 'Praça C, 789');

insert into funcionarios (id, nome, cargo, login, senha) values
(1, 'Carlos Lima', 'Vendedor', 'carlos', 'senha123'),
(2, 'Fernanda Souza', 'Administrador', 'fernanda', 'senha456'),
(3, 'Lucas Almeida', 'Vendedor', 'lucas', 'senha789');

insert into produtos (id, nome, descricao, preco, estoque) values
(1, 'Notebook', 'Notebook Dell', 3500.00, 10),
(2, 'Smartphone', 'Smartphone Samsung', 2500.00, 20),
(3, 'Tablet', 'Tablet Xiaomi', 1500.00, 15);

insert into vendas (id, clienteID, funcionarioID, formaPagamento, parcelas, total) values
(1, 1, 1, 'à vista', 1, 5000.00),
(2, 2, 2, 'parcelado', 3, 2500.00);

insert into itensVenda (id, vendaID, produtoID, quantidade, preco) values
(1, 1, 1, 1, 3500.00),
(2, 1, 3, 1, 1500.00),
(3, 2, 2, 1, 2500.00);

select
    clientes.nome AS NomeCliente,
    funcionarios.nome AS NomeVendedor,
    produtos.nome AS ProdutoComprado,
    itensVenda.preco * ItensVenda.quantidade AS ValorTransacao,
    Vendas.dataVenda
FROM Vendas
JOIN Clientes ON Vendas.clienteID = Clientes.id
JOIN Funcionarios ON Vendas.funcionarioID = Funcionarios.id
JOIN ItensVenda ON Vendas.id = ItensVenda.vendaID
JOIN Produtos ON ItensVenda.produtoID = Produtos.id;