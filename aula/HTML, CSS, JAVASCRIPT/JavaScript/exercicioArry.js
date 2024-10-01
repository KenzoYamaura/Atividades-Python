
var array1 = [1, 2, 3, 4, 5];
var array2 = [5, 6, 7, 8, 9, 10];


var array3 = [new Set([...array1, ...array2])];

console.log(array3)