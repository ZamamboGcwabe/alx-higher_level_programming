#!/usr/bin/node

function factorial(num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Please provide a valid number');
} else {
  const result = factorial(num);
  console.log('The factorial of ${num} is ${result}');
}
