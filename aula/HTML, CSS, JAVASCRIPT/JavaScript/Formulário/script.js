
const form = document.getElementById("form")
const usuario = document.getElementById("usuario")
const email = document.getElementById("email")
const senha = document.getElementById("senha")
const senha2 = document.getElementById("senha2")

function showError(input, mensagem) {

    const formControl = input.parentElement
    formControl.className = "form-control error"
    const small = formControl.querySelector("small")
    small.innerHTML = mensagem

}

function showSucesso(input, mensagem) {

    const formControl = input.parentElement
    formControl.className = "form-control sucesso"

}

function checkRequired(listaInput) {

    let valido = true
    listaInput.forEach(function (input) {
        if (input.value == "") {
            showError(input, "Campo Obrigatório")
            valido = false
        } else {
            showSucesso(input)
        }
    })
    return valido
}

function checkSize(input, max, min) {
    let valido = true
    if (input.value.length < min) {
        showError(input, `Tente quer no mínimo ${min}`)
        valido = false
    } else if (input.value.length > max) {
        showError(input, `Maior que ${max}`)
        valido = false
    }
    return valido
}

function checkPassaword(senha, senha2) {
    if (senha.value !== senha2.value) {
        showError(senha2, "As senhas não são iguais")
        return false
    }
    return true
}

form.addEventListener("submit", function (event) {
    event.preventDefault()

    let isValid = checkRequired([usuario, email, senha, senha2])

    isValid = checkSize(usuario, 15, 3) && isValid
    isValid = checkSize(senha, 15, 3) && isValid

    isValid = checkPassaword(senha, senha2) && isValid

    if(isValid){
        const dados = {
            usuarioNome: usuario.value,
            usuarioEmail: email.value,
            usuarioSenha: senha.value
        } 
        console.log(dados)           

        window.location.href = "./home.html"
    }
})