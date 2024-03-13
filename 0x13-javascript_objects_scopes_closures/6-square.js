#!/usr/bin/node

const square = require("./5-square");

class Square extends square {
	constructor(size) {
		super(size);
	}

	charPrint(c="x") {
	    for (let i = 0; i < this.height; i++) {
	      console.log(c.repeat(this.width));
	    }
	}
}

module.exports = Square;
