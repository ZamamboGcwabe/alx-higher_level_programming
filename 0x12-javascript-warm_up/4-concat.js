#!/usr/bin/node

const [arg1, arg2] = process.argv.slice(2);

console.log(`${arg1 || 'undefined'} is ${arg2 || 'undefined'}`);
