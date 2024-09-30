let x;

const arr = [28, 38, 44, 29, 109];

// push() - Adiciona um valor ao final do array
arr.push(100);

// pop() - Remove o último valor
arr.pop();

// unshift() - Adiciona um valor ao início do array
arr.unshift(99);

// shift() - Remove o primeiro valor
arr.shift();

// reverse() - Inverte o array
arr.reverse();

// includes() - Verifica se algo está no array
x = arr.includes(445);

// indexOf() - Retorna o índice da primeira correspondência
x = arr.indexOf(28);

// Retorna o array como uma string
x = arr.toString();
x = arr.join();

// slice() retorna elementos selecionados em um array, como um novo array. Slice recebe o índice do primeiro elemento e o índice do último elemento a ser incluído no novo array.
x = arr.slice(1, 4);

// splice() funciona como slice(), exceto que recebe o índice do primeiro elemento e o número de elementos a seguir como segundo argumento. Ele também altera o array original, ao contrário do slice(), que não o faz.
x = arr.splice(1, 4);

// Remove um único elemento/valor - O seguinte irá alterar o array original, removendo o elemento com o índice 4. x será igual a um novo array com esse valor retirado.
x = arr.splice(4, 1);

// Encadeamento de métodos - Alguns métodos podem ser encadeados dependendo do valor de retorno.
x = arr.slice(1, 4).reverse().toString().charAt(0);

console.log(x);
