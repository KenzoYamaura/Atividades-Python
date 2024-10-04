create database exercicio_join_1;

use exercicio_join_1;

create table Funcionarios(
	idFuncionario int primary key,
    nome varchar(45),
    sobrenome varchar(45),
    id_departamento int,
    foreign key(id_departamento) references Departamentos(idDepartamento)
);

create table Departamentos(
	idDepartamento int not null primary key,
    nome_departamento varchar(50),
    localizacao varchar(50)	
);

insert into Funcionarios(idFuncionario, nome, sobrenome, id_departamento) values
(1, 'João', 'Silva', 1),
(2, 'Maria', 'Santos', 2),
(3, 'Pedro', 'Ferreira', 1),
(4, 'Ana', 'Oliveira', 3);

insert into Departamentos(idDepartamento, nome_departamento, localizacao) values
(1, 'Vendas', 'São Paulo'),
(2, 'Marketing', 'Rio de Janeiro'),
(3, 'TI', 'Belo Horizonte');

select Funcionarios.nome, Funcionarios.sobrenome, Departamentos.nome_departamento, Departamentos.localizacao 
from Funcionarios join Departamentos on Funcionarios.idFuncionario = Departamentos.idDepartamento;



