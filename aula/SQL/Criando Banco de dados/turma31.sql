CREATE DATABASE turma31;

use turma31;

create table usuario(
	id int not null primary key auto_increment,
	nome varchar(45) not null,
    senha varchar(100) not null
);

insert into usuario(nome, senha) values
("Kenzo", "223344");

drop database turma31;