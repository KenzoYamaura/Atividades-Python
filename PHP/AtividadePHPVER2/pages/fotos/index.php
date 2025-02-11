<?php
require __DIR__ . "/../../backend/controller/fileController.php";

$fileController = new FileController();
$listaImagem = $fileController->getAllImagem();


?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <form action="../../backend/router/fileRouter.php?acao=salvarImagem" method="POST" enctype="multipart/form-data">
        <label for="escolher">
            Escolher Foto
        </label>
        <input style="display:none" id="escolher" type="file" name="image">
        <button type="submit">Enviar</button>
    </form>

    <?php
        foreach($listaImagem as $item){
    ?> 
        <img width="100px" height="100px" src="../../public/uploads/<?php echo $item["nome"]?>" alt="">
    <?php
        }
    ?>


</body>

</html>