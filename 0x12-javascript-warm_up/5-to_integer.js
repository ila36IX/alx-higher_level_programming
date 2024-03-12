#!/usr/bin/node

const { argv } = require('node:process');

if (!Number(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(Number(argv[2])));
}
