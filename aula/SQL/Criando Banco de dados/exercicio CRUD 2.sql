create database exercicio2_cruds;

use exercicio2_cruds;

create table medicamentos(
	medicamentoid int not null primary key auto_increment,
    nome varchar(50) not null,
    fabricante varchar(50) not null,
    preco decimal(10,2) not null,
    quantidade_em_estoque int not null
);

create table clientes(
	clienteid int not null primary key auto_increment,
    nome varchar(50) not null,
    endereco varchar(50) not null,
    telefone varchar(20) not null
);

create table vendas(
	vendaid int not null primary key auto_increment,
    id_clientes int not null,
    foreign key(id_clientes) references clientes(clienteid),
    data_da_venda date not null
);

create table itens_de_venda(
	itemid int not null primary key auto_increment,
    id_vendas int not null,
    foreign key(id_vendas) references vendas(vendaid),
    id_medicamentos int not null,
    foreign key(id_medicamentos) references medicamentos(medicamentoid),
    quantidade int not null,
    precototal decimal(10,2)
);

insert into medicamentos(nome, fabricante, preco, quantidade_em_estoque)
values('Paracetamol','Farmaco', 5.99, 100),
	  ('Amoxicilina','PharmaCorp', 8.50, 50),
      ('Omeprazol','MegaMed', 7.25, 80);
      
insert into clientes(nome, endereco, telefone)
values('Maria Silva', 'Rua A, 123', '555-1234'),
      ('João Santos', 'Av. B, 456', '555-5678');
	
insert into vendas(id_clientes, data_da_venda)
values(1,'2023-10-10'),
      (2,'2023-10-11');
      
insert into itens_de_venda(id_vendas, id_medicamentos, quantidade, precototal)
values(1, 1, 2, 11.98),
      (1, 2, 3, 25.50);
	
-- update cliente set email = "asad" where id = 0

update medicamentos set preco = 6.50 where medicamentoid = 1;
update clientes set endereco = "Rua X, 109" where clienteid = 2;
update medicamentos set quantidade_em_estoque = 100 where medicamentoid = 3;

select * from medicamentos where fabricante = 'PharmaCorp' or fabricante = 'MegaMed';





      
	