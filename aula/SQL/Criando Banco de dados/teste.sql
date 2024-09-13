create database test123;

use test123;

show tables;

create table pessoa(
	id int not null,
    nome varchar(100) not null,
    cpf char(11) not null unique,
    idade int not null,
    primary key (id)
);

create table venda(
	id int not null primary key,
    produto varchar(55),
    id_pessoa int not null,
    foreign key(id_pessoa) references pessoa(id)
);
