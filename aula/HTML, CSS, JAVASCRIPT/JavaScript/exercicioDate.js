var dataHoje = new Date()
var dataNascimento = new Date("2000/01/01")

function idade(dataNascimento) {
    let idade = 0
    if (dataHoje.getFullYear() >= dataNascimento.getFullYear()) {
        idade = idade + (dataHoje.getFullYear() - dataNascimento.getFullYear())

    } if (dataHoje.getDate() < dataNascimento.getDate()) {
        idade -= 1

    } if (dataHoje.getMonth() < dataNascimento.getMonth()) {
        idade -= 1
    } return idade
}

console.log(idade(dataNascimento))