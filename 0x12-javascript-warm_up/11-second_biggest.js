#!/usr/bin/node

const { argv } = require('node:process');
function maxSecond (a) {
  if (a.length <= 2 || a.length === 3) {
    return (0);
  }
  let max = -Infinity;
  let secondMax = -Infinity;

  for (const i of a) {
    if (+i > max) {
      if (secondMax < max) {
        secondMax = max;
      }
      max = +i;
    }
  }
  return (secondMax);
}

const a = argv;

console.log(maxSecond(a));
