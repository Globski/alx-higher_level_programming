#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
