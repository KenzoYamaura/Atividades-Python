
var array1 = [1, 2, 3, 4, 5, 5, 5, 5, 5];
var array2 = [5, 6, 7, 8, 9, 10];

function juntar(array1, array2) {
    var array3 = [...array1, ...array2]
    for (let i = 0; i < array3.length; i++) {
        for (let j = i + 1; j < array3.length; j++) {
            if (array3[i] == array3[j]) {
                array3.splice(j, 1)
                j -= 1
            }
        }
    }
    return array3
}

console.log(juntar(array1, array2))
