#!/usr/bin/node

function factorial (n) {
  if (Number.isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2], 10);
const result = factorial(num);
console.log(result);
