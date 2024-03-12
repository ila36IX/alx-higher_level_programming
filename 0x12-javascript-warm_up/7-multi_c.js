#!/usr/bin/node

const { argv } = require('node:process');

if (!Number(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let manyTimes = Number(argv[2]);
  while (manyTimes > 0) {
    console.log('C is fun');
    manyTimes--;
  }
}
