create database exercicio_join_2;

use exercicio_join_2;

create table Alunos(
	id_alunos int not null auto_increment primary key,
    nome varchar(45) not null,
    sobrenome varchar(45) not null
);

create table Disciplinas(
	id_disciplinas int not null auto_increment primary key,
    nome_disciplina varchar(45) not null,
    codigo_disciplina varchar(45) not null
);

create table Notas(
	id_notas int not null auto_increment primary key,
    alunosId int,
    foreign key(alunosId) references Alunos(id_alunos),
    disciplinasId int,
    foreign key(disciplinasId) references Disciplinas(id_disciplinas),
    nota_alunos decimal(10,2)
);

insert into Alunos(nome, sobrenome) values
('Carlos', 'Silva'),
('Ana', 'Ferreira'),
('Paulo', 'Santos');

insert into Disciplinas(nome_disciplina, codigo_disciplina) values
('História', 'HIS102'), 
('Ciências', 'CIE103');

insert into Notas(id_notas, alunosId, disciplinasId, nota_alunos) values
(1001, 1, 101, 90.5), 
(1002, 1, 102, 85.0), 
(1003, 2, 101, 88.5), 
(1004, 2, 102, 92.0), 
(1005, 3, 101, 78.0), 
(1006, 3, 103, 96.5);


select Alunos.nome, Alunos.sobrenome, Disciplinas.nome_disciplina, Disciplinas.codigo_disciplina, Notas.nota_alunos
from Notas join Alunos ON Notas.alunosId = Alunos.id_alunos 
join Disciplinas ON Notas.disciplinasId = Disciplinas.id_disciplinas;







