#!/usr/bin/node

const list = require('./101-data').dict;

const newObj = {};

Object.entries(list).forEach(([key, value]) => {
  newObj[value] ? newObj[value].push(key) : newObj[value] = [key];
});
console.log(newObj);
