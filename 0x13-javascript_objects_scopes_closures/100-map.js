#!/usr/bin/node

const list = require('./100-data.js').list;

const factorIndex = list.map((item, idx) => item * idx);
console.log(list);
console.log(factorIndex);
