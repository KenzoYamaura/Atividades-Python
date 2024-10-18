create database exercicio_join_4;

use exercicio_join_4;

select * from Livros;
select * from Autores;
select * from Emprestimo;

create table Livros (
	idLivro int not null auto_increment primary key,
    titulo varchar(45),
    autorId int,
    foreign key (autorId) references Autores(idAutor),
    quantidadeExemplares int
);

create table Autores (
	idAutor int not null auto_increment primary key,
    nome varchar(45),
    nacionalidade varchar(45)
);

create table Emprestimo (
	idEmprestimo int not null auto_increment primary key,
    nome_cliente varchar(45),
    livroId int,
    foreign key(livroId) references Livros(idLivro),
    data_emprestimo date,
    data_devolucao date
);

insert into Livros(idLivro, titulo, autorId, quantidadeExemplares) values
(null, 'Harry Potter and the Sorcerer s Stone', 1, 5),
(null, '1984', 2, 3), 
(null, 'Pride and Prejudice', 3, 4),
(null, 'The Adventures of Huckleberry Finn', 4, 6);

insert into Autores(idAutor, nome, nacionalidade) values
(null, 'J.K. Rowling', 'Reino Unido'),
(null, 'George Orwell', 'Reino Unido'), 
(null, 'Jane Austen', 'Reino Unido'), 
(null, 'Mark Twain', 'Estados Unidos');

insert into Emprestimo(idEmprestimo, nome_cliente, livroId, data_emprestimo, data_devolucao) values
(null, 'João', 1, '2023-10-01', NULL),
(null, 'Marcela', 3, '2023-10-02', NULL), 
(null, 'Pedro', 4, '2023-10-03', NULL),
(null, 'Ana', 2, '2023-09-15', '2023-09-30'), 
(null, 'Carlos', 1, '2023-09-20', '2023-10-05');

select Livros.titulo, Livros.autorId, Emprestimo.nome_cliente, Emprestimo.data_emprestimo
from Livros join Emprestimo on Livros.Idlivro = Emprestimo.livroId where Emprestimo.data_devolucao is null;










