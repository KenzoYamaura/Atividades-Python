<?php
session_start();
if (!$_SESSION["id_usuario"]){
    header("Location: ../../index.php");
}

require_once __DIR__ . "/../../backend/controller/userController.php";

$userController = new UserController();

$usuario = [
    "id" => "",
    "nome" => "",
    "senha" => ""
];

$acao = "cadastrar";
$TituloBotao = "Cadastrar";
if(isset($_GET["id"])){
    $id = $_GET["id"];
    $acao = "update";
    $TituloBotao = "Editar";
    $usuario = $userController->GetUserById($id);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="<?php echo "../../backend/router/userRouter.php?acao=$acao" ?>" method="POST">
        <input type="hidden" name="idUsuario" value="<?php echo $usuario["id"] ?>">
        <input type="text" name="nome" placeholder="Nome" value="<?php echo $usuario["nome"]?>">
        <input type="text" name="senha" placeholder="Password" value="<?php echo $usuario["senha"]?>">
        <button type="submit"><?php echo $TituloBotao?></button>
    </form>


</body>
</html>