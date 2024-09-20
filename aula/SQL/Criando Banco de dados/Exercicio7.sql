create database exercicio7;

use exercicio7;
show tables;

create table fornecedor(
	codigo_fornecedor int not null primary key,
    nome varchar(45),
    CNPJ varchar(20) not null,
    endereco varchar(60)
);

create table fornecedor_has_produto(
	fornecedor_codigo int not null,
    foreign key(fornecedor_codigo) references fornecedor(codigo_fornecedor),
    codigo_produto int not null,
    foreign key(codigo_produto) references produto(codigo_produto)    
);

create table produto(
	codigo_produto int not null primary key,
    nome varchar(45) not null,
    descricao varchar(254)
);

create table produto_has_venda(
	produto_codigo int not null,
    foreign key(produto_codigo) references produto(codigo_produto),
    venda_num_notafiscal int not null,
    foreign key(venda_num_notafiscal) references venda(num_notafiscal),
    venda_loja_codigo int not null,
    foreign key(venda_loja_codigo) references venda(loja_codigo),
    venda_cliente_codigo int not null,
    foreign key(venda_cliente_codigo) references venda(cliente_codigo),
    preco decimal(10,2) not null,
    quantidade int not null
);

create table venda(
	num_notafiscal int not null primary key,
    data_venda date not null,
    valor_total decimal(10,2),
    loja_codigo int not null,
    foreign key(loja_codigo) references loja(codigo_loja),
    cliente_codigo int not null,
    foreign key(cliente_codigo) references cliente(codigo_cliente)
);

create table cliente(
	codigo_cliente int not null primary key,
    nome varchar(45),
    endereco varchar(60)
);

create table loja(
	codigo_loja int not null primary key,
    nome varchar(45) not null,
    CNPJ varchar(45) not null    
);

