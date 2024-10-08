
var x = document.getElementById("botão")
x.innerHTML = "Butão"

const newElement = document.createElement("p")


x.addEventListener("click", function () {

    let y = document.getElementById("texto")
    newElement.innerHTML = "Lorem ipsum dolor sit"

    y.appendChild(newElement)
    
})


