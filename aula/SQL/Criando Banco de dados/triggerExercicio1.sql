CREATE DATABASE triggerExercicio1;

drop DATABASE triggerExercicio1;

use triggerExercicio1;

CREATE TABLE Comentarios (
	id_comentario INT PRIMARY KEY,
    fk_id_postagem INT,
    foreign key(fk_id_postagem) references Estatisticas_Postagem (id_postagem),
    comentario TEXT
);

CREATE TABLE Estatisticas_Postagem (
	id_postagem INT PRIMARY KEY,
    titulo varchar(100),
    contador_comentarios INT DEFAULT 0
);

DELIMITER $
create trigger Del_Comentario after delete
on Comentarios
for each row
begin
	UPDATE Estatisticas_Postagem SET contador_comentarios = contador_comentarios - 1
    WHERE id_postagem = OLD.fk_id_postagem;
end ;
$
DELIMITER ;

select * from Comentarios;

select * from Estatisticas_Postagem;

insert into Comentarios (id_comentario, fk_id_postagem, comentario) VALUES
(1, 1, "DKAPOS"),
(2, 2, "kakak"),
(3, 3, "hahah");

insert into Estatisticas_Postagem (id_postagem, titulo, contador_comentarios) VALUES
(1, "oi", 5),
(2, "owwwi", 5),
(3, "owi", 5);

delete from Comentarios where id_comentario = 3;