#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

if (!isNaN(Number(firstArg))) {
  console.log(`My number: ${parseInt(firstArg)}`);
} else {
  console.log("Not a number");
}
