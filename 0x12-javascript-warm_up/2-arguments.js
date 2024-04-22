#!/usr/bin/node

const argslength = process.argv.length;

if (argslength === 2) {
	console.log("No argumen");
} else if (argslength === 3) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
