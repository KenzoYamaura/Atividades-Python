var botao = document.getElementById("Cadastrar")
var bemVindo = document.getElementById("bemVindo")
var msg = document.createElement("p")


botao.addEventListener("click", function () {

    var userName = document.getElementById("user").value
    let userSenha = document.getElementById("password").value

    msg.innerHTML = ""

    if(userName == "admin" && userSenha == "admin"){
        msg.innerHTML = "Bem-Vindo ADM";
        msg.style.color = "green";
        bemVindo.appendChild(msg);
    }    
    else{
        msg.innerHTML = "Usuário ou Senha Incorreto"
        msg.style.color = "red";
        bemVindo.appendChild(msg)
    }
})