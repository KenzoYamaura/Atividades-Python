create database estudo_caso1;

use estudo_caso1;

show tables;

describe medicos;
describe consultas;
describe pacientes;
describe exames;

create table medicos(
	CRM int not null auto_increment primary key,
    nome varchar(45) not null,
    endereco varchar(45) not null,
    telefone varchar(11) not null,
    especialidade varchar(45)
);

create table consultas(
	idconsultas int not null auto_increment primary key,
    obs text(255) not null,
    data_consulta date not null,
    hora time not null
);

create table pacientes(
	CPF varchar(45) not null primary key,
    nome varchar(45) not null,
    endereco varchar(45) not null,
    telefone varchar(45) not null
);

create table exames(
	idexames int not null primary key,
    nome varchar(45) not null,
    tipo varchar(45) not null,
    resultado text(255) not null
);

