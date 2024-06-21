#!/usr/bin/node

const process = require('node:process');

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }

  if (a < 0) {
    return;
  } else if (a === 0 || a === 1) {
    return (1);
  }

  return a * factorial(a - 1);
}

const a = +process.argv[2];

console.log(factorial(a));
