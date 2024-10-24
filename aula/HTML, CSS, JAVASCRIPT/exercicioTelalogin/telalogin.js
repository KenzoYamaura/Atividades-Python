
const email = document.getElementById("email")
const senha = document.getElementById("senha")
const botao = document.getElementById("entrar")

function MostrarErro(input, mensagem) {

    const control = input.parentElement
    control.className = "control error"
    const small = document.querySelector("small")
    small.innerHTML = mensagem
}

function MostrarSucesso(input) {

    const control = input.parentElement
    control.className = "control sucesso"
}

function veriSize(input, maximo, minimo) {

    let valido = true
    if (input.value.length < minimo) {
        MostrarErro(input, `Ter no mínimo ${minimo}`)
        valido = false
    } else if (input.value.length > maximo) {
        MostrarErro(input, `Maior que ${maximo}`)
        valido = false
    }
    return valido
}


function verificarRequerimento(inputListas) {

    let valid = true
    inputListas.forEach(function (input) {
        if (input.value = "") {
            MostrarErro(input, "Campo Obrigatório")
            valid = false
        } else {
            MostrarSucesso(input)
        }

    })
    return valid
}

botao.addEventListener("submit", function (event) {
    event.preventDefault()

    let validacao = verificarRequerimento([email, senha])

    validacao = veriSize(usuario, 15, 3) && validacao
    validacao = veriSize(senha, 15, 3) && validacao

    console.log("opijkad")
})

