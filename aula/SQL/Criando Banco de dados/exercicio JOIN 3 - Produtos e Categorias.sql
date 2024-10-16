create database exercicio_join_3;

use exercicio_join_3;

select * from Produtos;
select * from Categorias;

create table Produtos(
	id_produto int not null auto_increment primary key,
    nome varchar(45) not null,
    preco decimal(10,2),
    id_categoria int,
    foreign key(id_categoria) references Categorias(categoria_id)    
);

create table Categorias(
	categoria_id int not null auto_increment primary key,
    nome varchar(45),
    descricao varchar(50)
);

insert into Categorias(categoria_id, nome, descricao) values
(1, 'Roupas', 'Roupas masculinas e femininas'), 
(2, 'Acessórios', 'Acessórios de prata');

insert into Produtos(id_produto, nome, preco, id_categoria) values
(1, 'Camiseta', 20.00, 1), 
(2, 'Calça', 30.00, 2), 
(3, 'Tênis', 50.00, 1), 
(4, 'Bolsa', 40.00, 2);

select Produtos.nome, Produtos.preco, Categorias.nome, Categorias.descricao
from Produtos join Categorias on Categorias.categoria_id = Produtos.id_categoria;













