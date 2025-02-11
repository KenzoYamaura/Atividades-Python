<?php

require_once __DIR__."/../controller/fileController.php";

$filecontroller = new FileController();

if($_SERVER["REQUEST_METHOD"] == "POST") {
    
    switch ($_GET["acao"]) {
        case 'salvarImagem':
            $uploadDir = "../../public/uploads/";                                                                                                                                       
            $tiposPermitidos = ["image/png", "image/jpeg", "image/jpg"];
            $image = $_FILES["image"];
                      
            
            if(!is_dir($uploadDir)){
                mkdir($uploadDir, 0777, true);
            }

            if(isset($image) && in_array($image["type"], $tiposPermitidos)){
                $caminhoTemp = $image["tmp_name"];
                $nomeFoto = $image["name"];
                $extensao = pathinfo($nomeFoto, PATHINFO_EXTENSION);                
                $novoNome = uniqid() . "." . $extensao;
                $destino = $uploadDir . $novoNome;

                if(move_uploaded_file($caminhoTemp, $destino)){
                    $resultado = $filecontroller->SalvarImagem($novoNome);
                    header("Location: ../../pages/fotos/index.php");

                }
            }

            break;
        
        default:  
            echo "não achei nenhuma opção";          
            break;
    }
}   