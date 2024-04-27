#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

const file = argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  err && console.log(err);
  data && console.log(data);
});
