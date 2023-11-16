#!/usr/bin/node
let biggest = 0;
let i;
const arrNumbers = [];

for (i =2; i < process.argv.length; i++) {
    if (Number.isNaN(parseInt(process.argv[i]) === false)) {
        arrNumbers[i - 2] = parseInt(process.argv[i]);
    }
}

if (arrNumbers.length > 1) {
    biggest = Math.max.apply(null, arrNumbers);
    i = arrNumbers.indexOf(biggest);
    arrNumbers[i] = -Infinity;
    biggest = Math.max.apply(null, arrNumbers);
}

console.log(biggest);