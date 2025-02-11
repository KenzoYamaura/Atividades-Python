<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <form action="./backend/router/loginRouter.php?acao=validarLogin" method="post">
        <label>Nome</label>
        <input type="text" name="nome" id="nome">
        <label>Senha</label>
        <input type="password" name="senha" id="senha">
        <button type="submit">Logar</button>
    </form>

</body>
</html>
