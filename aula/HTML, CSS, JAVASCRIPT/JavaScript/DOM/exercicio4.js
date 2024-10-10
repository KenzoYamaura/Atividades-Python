
var botao = document.getElementById("botao")

botao.addEventListener("click", function () {
    let input = document.getElementById("addItem")

    if (input.value !== "") {
        let l = document.createElement("li")
        let lista = document.getElementById("ul")
        let botaozin = document.createElement("button")

        botaozin.innerHTML = "Remove"
        botaozin.style.margin = "10px"

        l.innerHTML = input.value

        lista.appendChild(l)
        l.appendChild(botaozin)

        input.value = ""

        botaozin.addEventListener("click", function () {
            lista.removeChild(l)
        })
        
    } else{
        alert("Preencha o Campo")
    }

});
