#!/usr/bin/node

function add(a, b) {
  """
  This function adds two integers and returns the sum.

  Args:
      a: The first integer.
      b: The second integer.

  Returns:
      The sum of a and b.
  """
  return a + b;
}

const num1 = 5;
const num2 = 3;
const result = add(num1, num2);
console.log(`The sum of ${num1} and ${num2} is ${result}`);
