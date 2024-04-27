#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

const file = argv[2];
const data = argv[3];

fs.writeFile(file, data, 'utf8', function (err) {
  if (err) console.log(err);
});
