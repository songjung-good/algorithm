const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
    a = Number(input[0])
    b = Number(input[1])
    
    
}).on('close', function () {
    console.log(`a = ${a}`)
    console.log(`b = ${b}`)
});