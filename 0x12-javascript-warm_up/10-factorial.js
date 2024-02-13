#!/usr/bin/node

const { argv } = require('node:process');

const calcFactorail = function (num) {
  if (!num || num === 1) {
    return (1);
  } else {
    return num * calcFactorail(num - 1);
  }
};

console.log(calcFactorail(Number(argv[2])));
