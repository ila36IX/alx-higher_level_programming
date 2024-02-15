#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const arrayOfNumbers = argv.slice(2).map(val => Number(val)).sort((a, b) => b - a);
  console.log(arrayOfNumbers[1]);
}
