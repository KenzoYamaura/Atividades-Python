create database sistema_reservas;

use sistema_reservas;

create table espacos(
	idEspaço int not null primary key,
    nome varchar(100),
    tipo varchar(50),
    capacidade int not null,
    descricao text
);

create table usuarios(
	idUsuarios int not null primary key,
    nome varchar(100),
    email varchar(50),
    telefone varchar(10)
);

create table reserva(
	idReserva int not null primary key,
    
);