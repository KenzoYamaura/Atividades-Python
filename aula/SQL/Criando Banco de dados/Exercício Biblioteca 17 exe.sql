CREATE DATABASE Biblioteca;

USE Biblioteca;

CREATE TABLE Autores (
 autor_id INT AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 pais VARCHAR(50)
);

CREATE TABLE Categorias (
 categoria_id INT AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(50) NOT NULL
);

CREATE TABLE Livros (
 livro_id INT AUTO_INCREMENT PRIMARY KEY,
 titulo VARCHAR(200) NOT NULL,
 autor_id INT,
 categoria_id INT,
 preco DECIMAL(10, 2) NOT NULL,
 estoque INT NOT NULL,
 FOREIGN KEY (autor_id) REFERENCES Autores(autor_id),
 FOREIGN KEY (categoria_id) REFERENCES Categorias(categoria_id)
);

CREATE TABLE Membros (
 membro_id INT AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 endereco VARCHAR(200),
 telefone VARCHAR(20)
);

CREATE TABLE Emprestimos (
 emprestimo_id INT AUTO_INCREMENT PRIMARY KEY,
 livro_id INT,
 membro_id INT,
 data_emprestimo DATE NOT NULL,
 data_devolucao DATE,
 FOREIGN KEY (livro_id) REFERENCES Livros(livro_id),
 FOREIGN KEY (membro_id) REFERENCES Membros(membro_id)
);

INSERT INTO Autores (nome, pais) VALUES
('George Orwell', 'Reino Unido'),
('J.K. Rowling', 'Reino Unido'),
('Gabriel Garcia Marquez', 'Colômbia'),
('J.R.R. Tolkien', 'Reino Unido');

INSERT INTO Categorias (nome) VALUES
('Ficção Científica'),
('Fantasia'),
('Romance'),
('Biografia');

INSERT INTO Livros (titulo, autor_id, categoria_id, preco, estoque) VALUES
('1984', 1, 1, 35.90, 20),
('Harry Potter e a Pedra Filosofal', 2, 2, 49.90, 15),
('Cem Anos de Solidão', 3, 3, 42.50, 10),
('O Senhor dos Anéis', 4, 2, 75.00, 8);

INSERT INTO Membros (nome, endereco, telefone) VALUES
('João da Silva', 'Rua A, 123', '123456789'),
('Maria Oliveira', 'Rua B, 456', '987654321'),
('Carlos Souza', 'Rua C, 789', '1122334455');

INSERT INTO Emprestimos (livro_id, membro_id, data_emprestimo, data_devolucao) VALUES
(1, 1, '2023-09-10', '2023-09-20'),
(2, 2, '2023-09-12', '2023-09-22'),
(3, 3, '2023-09-15', NULL),
(4, 1, '2023-09-17', '2023-09-27');

-- 1 - Quais são os livros atualmente em estoque na biblioteca? --

select titulo, estoque from Livros;

-- 2 - Quais autores têm livros na biblioteca e de que países são? --

select Autores.nome, Autores.pais, Livros.titulo from 
Livros join Autores on Autores.autor_id = Livros.autor_id;

-- 3 - Qual é o preço de cada livro? --

select titulo, preco from Livros;

-- 4 - Quais membros pegaram livros emprestados? --

select Membros.nome from Emprestimos 
join Membros on Membros.membro_id = Emprestimos.membro_id group by membros.nome;

-- 5 - Quais livros foram emprestados até agora? -- 








