#!/usr/bin/node

const { argv } = require('node:process');
function maxSecond (a) {
  if (a.length <= 2 || a.length === 3) {
    return (0);
  }
  let max = -Infinity;
  let secondMax = -Infinity;

  /*for (const i of a) {
    if (+i > max) {
      let temp = max;
      max = +i;
      secondMax = max;
    }
  }*/

  for (let i = 2; i < a.length; i++) {
    if (+a[i] > max) {
        max = +a[i];
       // console.log(max);
    }
  }
  for (let i = 2; i < a.length; i++) {
    if (+a[i] > secondMax && +a[i] < max) {
        secondMax = +a[i];
    }
  }
  return (secondMax);
}

const a = argv;

console.log(maxSecond(a));
