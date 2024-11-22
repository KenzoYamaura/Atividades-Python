CREATE DATABASE escola;

use escola;

CREATE TABLE Alunos (
	id INT auto_increment primary key,
    nome varchar(100),
    idade int,
    curso varchar(50)
);

 select * from Alunos;
 
 CREATE TABLE Professores (
	id INT auto_increment primary key,
    nome varchar(100),
    disciplina varchar(50)
 );


