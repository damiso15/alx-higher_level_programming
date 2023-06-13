#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg, 10);
const str = 'C is fun';
let count = 0;

if (Number.isInteger(number)) {
  while (count < number) {
    console.log(str);
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
