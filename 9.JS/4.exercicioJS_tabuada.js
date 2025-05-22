const readlineSync = require('readline-sync')

let numero = parseInt(readlineSync.question("Digite um número para tabela: "))

console.log(`\nTabuada do ${numero}:`);
for (let i = 0; i <= 10; i++) {
    console.log(`${numero} x ${i} = ${numero * i}`);
}





