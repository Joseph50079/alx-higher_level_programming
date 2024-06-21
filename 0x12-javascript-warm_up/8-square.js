#!/usr/bin/node
const process = require('node:process');
const { argv } = require('node:process');

if (argv.length <= 2) {
  console.log('Missing size');
} else if (isNaN(+argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < +argv[2]; i++) {
    for (let i = 0; i < +argv[2]; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
