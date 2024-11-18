create database triggerExercicio2;

use triggerExercicio2;

CREATE TABLE Vendas(
	id_venda INT PRIMARY KEY, 
	fk_id_produto INT, 
	valor DECIMAL(10, 2), 
	FOREIGN KEY (fk_id_produto) REFERENCES
	Produtos(id_produto)
);

CREATE TABLE Total_Vendas (
	id_total_vendas INT PRIMARY KEY,
	total DECIMAL(10, 2)
);

CREATE TABLE Produtos ( 
	id_produto INT PRIMARY KEY, 
	nome VARCHAR(100), 
	quantidade INT, 
	preco DECIMAL(10, 2) 
);

delimiter $
create trigger Atualizar_Total_Vendas after update
on Vendas
for each row
begin
	update Total_Vendas
    set total = total + new.valor - old.valor
    where id_total_vendas = 1;
end$
delimiter ;

-- Inserindo dados na tabela Produtos
INSERT INTO Produtos (id_produto, nome, quantidade, preco) VALUES
(1, 'Produto A', 50, 20.00),
(2, 'Produto B', 30, 35.50),
(3, 'Produto C', 20, 15.75);

-- Inserindo dados na tabela Vendas
INSERT INTO Vendas (id_venda, fk_id_produto, valor) VALUES
(1, 1, 20.00),  -- Venda do Produto A
(2, 2, 35.50),  -- Venda do Produto B
(3, 3, 15.75),  -- Venda do Produto C
(4, 1, 20.00),  -- Outra venda do Produto A
(5, 2, 35.50);  -- Outra venda do Produto B

-- Inserindo dados na tabela Total_Vendas
INSERT INTO Total_Vendas (id_total_vendas, total) VALUES
(1, 126.75);  -- Total das vendas inseridas acima (exemplo)

update Vendas set valor = 80.00 where id_venda = 4;

select * from vendas;

select * from Total_Vendas;
