create database exercicio1_CRUDs;

use exercicio1_CRUDs;


create table clientes(
	id int not null primary key auto_increment,
    nome varchar(45) not null,
    email varchar(50) not null,
    telefone varchar(20) not null
);

insert into clientes(nome, email, telefone)
values('João Silva', 'joao@email.com','23456-7890'),
      ('Maria Santos', 'maria@email.com','87654-3210'),
      ('Amarildo Carlos Pereira', 'acarlos@email.com','75555-5555'),
      ('Ana Rodrigues', 'ana@email.com','77123-4567'),
      ('Pedro Oliveira', 'pedro@email.com','33888-9999');

-- Exercício – Selecione todos os clientes cujo nome comece com a letra 'A'.

select * from clientes where nome like "A%";

-- Atualize o número de telefone do cliente João Silva para '99867-0898'.

update clientes set telefone = '99867-0898' where id = 1;

-- Exclua todos clientes com número de telefone que possui inicial 7.

delete from clientes where telefone like '7%';


 



      
