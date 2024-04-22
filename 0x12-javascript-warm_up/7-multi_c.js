#!/usr/bin/node

const args = process.argv.slice(2);
const numOccurrences = parseInt(args[0);

if (isNaN(numOccurrences)) {
	console.log("Missing number of occurrences");
} else {
	for (let i = 0; i < numOccurrences; i++) {
		console.log("C is fun");
	}
}
