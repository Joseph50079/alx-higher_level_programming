#!/usr/bin/node

const { argv } = require('node:process');
function maxSecond (a) {
  if (a.length <= 2 || a.length === 3) {
    return (1);
  }
  let max = -Infinity;
  let secondMax = -Infinity;

  for (const i of a) {
    if (+i > max) {
      max = +i;
    } else if (i > secondMax && i !== max) {
      secondMax = +i;
    }
  }
  return (secondMax);
}

const a = argv;

console.log(maxSecond(a));
