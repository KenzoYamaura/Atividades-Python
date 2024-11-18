create database tabela_insercoes;

use tabela_insercoes;

create table produto (
	idProduto int not null primary key auto_increment,
    nome varchar(45),
    preco_normal decimal(10,2) not null,
    preco_desconto decimal(10,2) not null
);

DELIMITER //
create trigger atualizar_desc before insert
on produto
for each row
begin
set new.preco_desconto = (new.preco_normal * 0.90);
end; 
//
DELIMITER ;

insert into produto(nome, preco_normal)
values("Monitor", 600.00);

select * from produto;

