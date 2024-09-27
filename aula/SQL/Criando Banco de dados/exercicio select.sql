create database exercicio_select;

-- USANDO O BANCO EXERCICIO_SELECT -- 

use exercicio_select;

show tables;

create table produtos(
	id int not null primary key auto_increment,
    nome varchar(50),
    descricao text(255),
    preco decimal(10,2),
    quantidade int
);

insert into produtos(nome, descricao, preco, quantidade)
values("Camiseta", "Camiseta Branca de Algodão", 19.99, 50),
      ("tenis", "tenis esportivo preto", 49.99, 50),
      ("celular", "smartphone com tela oled", 399.99, 20);

-- trazer todos os produtos da tabela
select * from produtos;

-- uma consulta que retorne apenas produtos com preco maior que 20

select * from produtos where preco > 20.00;

-- consulta para trazer o preco máximo

select nome, preco from produtos where preco = (select MAX(preco) from produtos);

select sum(quantidade) from produtos;

select sum(quantidade) from produtos where (id = 1 or id = 2);

update produtos set preco = 24.99, quantidade = 120 where id = 1;

delete from produtos where id = 2;

select * from produtos;







