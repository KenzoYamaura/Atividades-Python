
var x = document.getElementById("botão")
x.innerHTML = "Click"

const newElement = document.createElement("p")

x.addEventListener("click", function () {

    const y = document.getElementsByClassName("texto")
    newElement.innerHTML = "Lorem ipsum dolor sit"

    y[0].appendChild(newElement)

    console.log("oi")

})


