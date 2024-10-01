
var lista = [1, 2, 3, 4, 5, 6]

function somaDosPares(lista){
    var soma = 0 
    for(let l = 0; l < lista.length; l++){
        if (lista[l] % 2 == 0){
            soma += lista[l]
        }
    }
    return soma
}

console.log(somaDosPares(lista))