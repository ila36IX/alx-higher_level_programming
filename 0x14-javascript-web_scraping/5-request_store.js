#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const fs = require('fs');

const url = argv[2];
const file = argv[3];

request(url, function (err, r, body) {
  if (!err && r.statusCode === 200) {
    fs.writeFileSync(file, body, 'utf8');
  }
});
