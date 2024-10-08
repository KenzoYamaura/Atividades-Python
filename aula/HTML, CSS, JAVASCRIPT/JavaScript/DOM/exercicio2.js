const button = document.getElementById("botao")
button.innerHTML = "Clique Aqui!!"

const div = document.getElementById("texto")

var cont = 0

button.addEventListener("click", function () {
    div.innerHTML = `Cliques: ${cont}`
    cont += 1
})
