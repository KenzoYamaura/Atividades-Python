// Criar uma nova instância representando a data e hora atuais
let x = new Date();
console.log(x)

//Converte um tipo data em string
let string = x.toString()
console.log(typeof string)

// Criar uma nova instância com base em uma string de data
let dataFromString = new Date('2023-12-07T12:00:00');
console.log(dataFromString)

z = new Date('2023-12-07T12:00:00');
console.log(z)

z = new Date('12/07/2023 12:00:00');
console.log(z)

z = new Date('12-07-2023 12:00:00');
console.log(z)

// Criar uma nova instância com base em valores específicos (ano, mês, dia, hora, minuto, segundo)
let dataPersonalizada = new Date(2023, 11, 7, 12, 0, 0); // Mês começa do zero (0 = janeiro, 11 = dezembro)
console.log(dataPersonalizada)

//Retorna o valor do ano da data em questão
y = x.getFullYear();
console.log(y)

//Retorna o valor do mês da data em questão
y = x.getMonth(); // Retorna um valor de 0 a 11
console.log(y)

//Retorna o dia da data em questão
y = x.getDate();
console.log(y)

// retorna a hora da data em questão
y = x.getHours();
console.log(y)

//Retorna o minutos da data em questão
y = x.getMinutes();
console.log(y)

//Retorna os segundos da data em questão
y = x.getSeconds();
console.log(y)


//Formatar datas, por padrão ele usa a linguagem do servidor 
console.log(x.toLocaleString()) //Retorna a representação da data formatada com horas
console.log(x.toLocaleDateString("pt-BR")); //Retonar a representação da data formatada sem as horas


//timeStamp é o valor da data em tempos, por padrão o timeStamp é em milisegundos
console.log(x.getTime())

//É possivel criar datas com timeStamps
console.log(new Date(x.getTime()));


//Criar formatação especifica.
let options = {
    weekday: 'long',
    year: '2-digit',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
}
console.log(x.toLocaleString('pt-BR', options))




