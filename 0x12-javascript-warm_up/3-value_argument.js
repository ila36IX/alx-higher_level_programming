#!/usr/bin/node

const { argv } = require('node:process');

let lengthOfArgv = 0;

argv.forEach(elem => {
  lengthOfArgv++;
});

if (lengthOfArgv <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
