create database sistemas_vendas;

use sistemas_vendas;

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

DELIMITER $$

CREATE TRIGGER AtualizaTotalVenda
AFTER INSERT ON itensVenda
FOR EACH ROW
BEGIN
    DECLARE novoTotal DECIMAL(10, 2);

    SELECT SUM(quantidade * preco) INTO novoTotal
    FROM itensVenda
    WHERE vendaID = NEW.vendaID;

    UPDATE vendas
    SET total = novoTotal
    WHERE id = NEW.vendaID;
END$$

DELIMITER ;

insert into clientes (id, nome, cpf, endereco) values
(1, 'Maria Silva', '12345678901', 'Rua A, 123'),
(2, 'João Santos', '23456789012', 'Avenida B, 456'),
(3, 'Ana Pereira', '12341424234', 'Praça C, 783'),
(4, 'Julho B', '13241246787', 'Rodovia MS, 3322'),
(5, 'Renato C', '41108967865', 'Rua Calógeras, 2312');

select * from clientes;

insert into funcionarios (id, nome, cargo, login, senha) values
(1, 'Carlos Lima', 'Vendedor', 'Carlos.L', '123'),
(2, 'Fernanda Souza', 'Administrador', 'Fernanda.S', '432'),
(3, 'Lucas Almeida', 'Vendedor', 'Lucas.A', '231'),
(4, 'Henrique Lima', 'Administrador', 'Henrique.L', '222'),
(5, 'Arthur Correa', 'Vendedor', 'Arthur.C', '111');

select * from funcionarios;

insert into produtos (id, nome, descricao, preco, estoque) values
(1, 'Notebook', 'Notebook Dell', 3500.00, 10),
(2, 'Smartphone', 'Smartphone Samsung', 2500.00, 20),
(3, 'Tablet', 'Tablet Xiaomi', 1500.00, 15),
(4, 'Mouse', 'Corsair', 300.00, 30),
(5, 'Processador', 'Ryzen 7600', 2500.00, 100),
(6, 'Placa de Vídeo', 'RTX 4070', 5500.00, 70);

select * from produtos;

INSERT INTO vendas (id, clienteID, funcionarioID, formaPagamento, parcelas) VALUES 
(1, 1, 1, 'à vista', 1), 
(2, 2, 2, 'parcelado', 3), 
(3, 3, 1, 'à vista', 1),
(4, 5, 3, 'parcelado', 2), 
(5, 4, 3, 'à vista', 2),
(6, 5, 5, 'parcelado', 2);

INSERT INTO itensVenda (id, vendaID, produtoID, quantidade, preco) VALUES 
(1, 1, 1, 3, 3500.00), 
(2, 2, 3, 1, 1500.00), 
(3, 3, 6, 2, 5500.00), 
(4, 4, 5, 1, 2500.00), 
(5, 5, 4, 5, 300.00),
(6, 6, 2, 10, 2500.00);


select
    clientes.nome as NomeCliente,
    funcionarios.nome as NomeVendedor,
    produtos.nome as ProdutoComprado,
    itensVenda.preco * itensVenda.quantidade as ValorTransacao,
    vendas.dataVenda
from vendas
join clientes on vendas.clienteID = clientes.id
join funcionarios on vendas.funcionarioID = funcionarios.id
join itensVenda on vendas.id = itensVenda.vendaID
join produtos on itensVenda.produtoID = produtos.id;
