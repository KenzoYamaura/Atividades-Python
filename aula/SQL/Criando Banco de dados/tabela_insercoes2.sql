create database tabela_insercoes2;

use tabela_insercoes2;

CREATE TABLE produtos (
	referencia varchar(3) primary key,
    descricao varchar(50) unique,
    estoque int not null default 0
);

create table itensvenda (
	venda int primary key,
    produto varchar(3),
    quantidade int not null
);

delimiter //
create trigger compra after insert
on itensvenda
for each row
begin
	update produtos set estoque = (estoque - new.quantidade)
    where referencia = new.produto;
end;

create trigger deletarcompra after delete
on itensvenda
for each row
begin
	update produtos set estoque = (estoque + old.quantidade)
    where referencia = old.produto;
end;
//
delimiter ;


INSERT INTO produtos VALUES ('001', 'Feijão',10);
INSERT INTO produtos VALUES ('002', 'Arroz',5);
INSERT INTO produtos VALUES ('003', 'Farinha',15);

INSERT INTO itensvenda VALUES (1, '001', 3);
INSERT INTO itensvenda VALUES (2, '002', 1);
INSERT INTO itensvenda VALUES (3, '003', 5);

select * from produtos;

drop database tabela_insercoes2;

