#!/usr/bin/node

<<<<<<< HEAD
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
=======
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
>>>>>>> f01b71021d62ef7e1f5c96d8f8ddc01178addedc
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
