create database lrjoin;

use lrjoin;

create table Clientes(
	id_cliente int primary key,
    nome varchar(45),
    email varchar(45)
);

insert into Clientes(id_cliente, nome, email) values
(1, "João", "joão@icloud.com"),
(2, "Maria", "maria@terra.com"),
(3, "Carlos", "carlos@gmail.com");

create table Pedidos(
	id_pedido int primary key,
    cliente_id int,
    foreign key(cliente_id) references Clientes(id_cliente),
    produto varchar(45)
);

insert into Pedidos(id_pedido, cliente_id, produto) values
(1, 1, "PRODUTO A"),
(2, 1, "PRODUTO B"),
(3, 2, "PRODUTO C");

select Clientes.id_cliente, Clientes.nome, Pedidos.produto
from Pedidos
right join Clientes on cliente_id = clientes.id_cliente;

select Clientes.id_cliente, Clientes.nome, Pedidos.produto
from Pedidos
cross join Clientes;