#!/usr/bin/node

function add(a, b) {
	const sum = a + b;
	console.log(sum);
}

const args = process.argv.slice(2);

if (args.length < 2) {
	console.log('Missing arguments');
} else {
	const firstNum = parseInt(args[0]);
	const secondNum = parseInt(args[1]);

	if (isNaN(firstNum) || isNaN(secondNum)) {
		console.log('Please provide valid numbers');
	} else {
		add(firstNum, secondNum);
	}
}

