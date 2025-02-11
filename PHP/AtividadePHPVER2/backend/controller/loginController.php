<?php
include_once __DIR__."/../db/database.php";

class LoginController
{
    private $conn;

    public function __construct(){
        $database = new Database();
        $this->conn = $database->connect();
    }

    public function Login($nome, $senha){
        try {
           $sql = "SELECT * FROM usuario where nome = :nome and senha = :senha";
           $db = $this->conn->prepare($sql);
           $db->bindParam(":nome", $nome);
           $db->bindParam(":senha", $senha);
           $db->execute();
           $usuario = $db->fetchALL(PDO::FETCH_ASSOC);

           if($usuario){
            session_start();
            $_SESSION["id_usuario"] = $usuario[0]["id"];
            return true;

           }else{
            return false;

           }

        } catch (\Exception $e) {
            echo "erro:".$e->getMessage();
            
        }
    }
}

?>