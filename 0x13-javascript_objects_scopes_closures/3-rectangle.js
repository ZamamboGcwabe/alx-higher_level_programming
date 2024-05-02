#!/usr/bin/node

class Rectangle {
<<<<<<< HEAD
  constructor (w, h) {
    if (width > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
=======
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	
	print () {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
>>>>>>> 6009b0164887701126fd47f6b8cda505956de661
}

module.exports = Rectangle;
