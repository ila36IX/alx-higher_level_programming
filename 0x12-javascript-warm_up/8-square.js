#!/usr/bin/node

const { argv } = require('node:process');

if (Number(argv[2]) || Number(argv[2]) === 0) {
  const size = Number(argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
