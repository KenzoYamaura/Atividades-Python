-- CREATE DATABASE turma31;

-- drop database turma31;

select * from usuario;

use turma31;

create table usuario(
	id int not null primary key auto_increment,
	nome varchar(45) not null,
    senha varchar(100) not null
);

create table imagens(
	id int auto_increment primary key,
    nome varchar(100)
);

insert into usuario(nome, senha) values
("Kenzo", "223344");

