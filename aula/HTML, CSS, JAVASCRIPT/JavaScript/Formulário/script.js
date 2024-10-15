
const form = document.getElementById("form")
const usuario = document.getElementById("usuario")
const email = document.getElementById("email")
const senha = document.getElementById("senha")
const senha2 = document.getElementById("senha2")

function showError(input, mensagem){
    const formControl = input.parentElement
    formControl.className = "form-control error"
    const small = formControl.querySelector("small")
    small.innerHTML = mensagem
}

function checkRequired(listaInput){

    listaInput.forEach(function(input) {
        if(input.value == ""){
            showError(input, "Campo Obrigatório")
        }
    })
}

form.addEventListener("submit", function(event){
    event.preventDefault()

    checkRequired([usuario, email, senha, senha2])
})