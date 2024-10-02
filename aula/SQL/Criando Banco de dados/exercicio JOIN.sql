create database vendas_join;

use vendas_join;

create table clientes(
	id int primary key,
    nome varchar(100),
    email varchar(100),
    telefone varchar(15)
);

create table vendas(
	id int primary key,
    cliente_id int,
    data_da_venda date,
    valor decimal(10,2),
    produto varchar(100),
    foreign key(cliente_id) references clientes(id)
);

insert into clientes (id, nome, email, telefone) values
(1, 'João Silva', 'joao@exemple.com', '123456789'),
(2, 'Maria Oliveira', 'maria@exemple.com', '987654321'),
(3, 'Carlos Santos', 'carlos@exemple.com', '456789123');

insert into vendas (id, cliente_id, data_da_venda, valor, produto) values
(1, 1, '2024-01-15', 150.00, 'Produto A'),
(2, 2, '2024-01-20', 200.00, 'Produto B'),
(3, 1, '2024-02-10', 300.00, 'Produto C'),
(4, 3, '2024-02-15', 100.00, 'Produto D');

select clientes.nome, clientes.telefone, vendas.valor, vendas.produto 
from clientes join vendas on clientes.id = vendas.cliente_id;

select clientes.nome, clientes.telefone, vendas.valor, vendas.produto 
from clientes join vendas on clientes.id = vendas.cliente_id where clientes.nome like 'João Silva';

select clientes.nome, SUM(vendas.valor) from clientes 
join vendas on clientes.id = vendas.cliente_id group by clientes.nome; 

select clientes.nome, clientes.telefone, vendas.data_da_venda, vendas.valor, vendas.produto from clientes 
join vendas on clientes.id = vendas.cliente_id where vendas.data_da_venda > '2024-01-31'; 



