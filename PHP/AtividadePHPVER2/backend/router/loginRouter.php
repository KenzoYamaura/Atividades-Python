<?php

require_once __DIR__."/../controller/loginController.php";

$logincontroller = new LoginController();

if($_SERVER["REQUEST_METHOD"] == "POST") {
    
    switch ($_GET["acao"]) {
        case 'validarLogin':
            $nome = $_POST["nome"];
            $senha = $_POST["senha"];

            if(!(empty($nome) || empty($senha))){
                $resposta = $logincontroller->Login($nome, $senha);
                if($resposta){
                    header("Location: ../../pages/home/index.php");
                }else {
                    header("Location: ../../index.php");
                }
            }
            break;
        
        default:  
            echo "não achei nenhuma opção";          
            break;
    }
}   