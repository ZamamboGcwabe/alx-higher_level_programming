#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0) {
      this.width = w;
    } else {
      throw new TypeError('width must be positive integer');
    }
    if (Number.isInteger(h) && h > 0) {
      this.height = h;
    } else {
      throw new TypeError('height must be positive integer');
    }
  }
}

module.exports = Rectangle;
