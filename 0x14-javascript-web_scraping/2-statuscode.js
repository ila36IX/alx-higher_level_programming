#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

const url = argv[2];
request
  .get(url)
  .on('response', (r) => {
    console.log(`code: ${r.statusCode}`);
  });
