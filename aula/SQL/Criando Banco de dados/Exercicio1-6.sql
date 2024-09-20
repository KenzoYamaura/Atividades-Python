create database exercicio6;

use exercicio6;

create table clientes(
	id_cliente int not null primary key,
    nome varchar(45) not null,
    sobrenome varchar(45) not null,
    email varchar(45) not null,
    data_nascimento date not null
);

create table produtos(
	id_produto int not null primary key,
    nome_produto varchar(45) not null,
    preco decimal(10,2),
    descricao varchar(254),
    categoria varchar(45)
);

create table pedidos(
	id_pedidos int not null primary key,
    data_pedido date,
    cliente_id int not null,
    foreign key(cliente_id) references clientes(id_cliente),
    status_pedido varchar(50)    
);

create table itenspedido(
	id_itenspedido int not null primary key,
    pedidos_id int not null,
    foreign key(pedidos_id) references pedidos(id_pedidos),
    produtos_id int not null,
    foreign key(produtos_id) references produtos(id_produto),
    quantidade varchar(50)    
);

create table categorias(
	id_categoria int not null primary key,
    nome_categoria varchar(50)
);

create table funcionarios(
	id_funcionarios int not null primary key,
    nome varchar(45) not null,
    sobrenome varchar(45) not null,
    cargo varchar(45) not null,
    data_contratacao date,
    salario decimal(10,2) not null
);