#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		this.width = (Number.isInteger(w) && w > 0) ? w : 0;
		this.height = (Number.isInteger(h) && h > 0) ? h : 0;
	}
}

module.exports = Rectangle
