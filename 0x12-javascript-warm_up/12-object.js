#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
const modifiedObject = {
  ...myObject,
  value: 89,
};

console.log(modifiedObject);
