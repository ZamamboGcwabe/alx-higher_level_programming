#!/usr/bin/node

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
