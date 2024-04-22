#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(num => parseInt(num));

if (numbers.length === 0) {
  console.log(0);
} else if (numbers.length === 1) {
  console.log(0);
} else {
  let largest = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      largest = numbers[i];
    }
  }
  let secondLargest = -Infinity;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] < largest && numbers[i] > secondLargest) {
      secondLargest = numbers[i];
    }
  }

  console.log(secondLargest);
}
