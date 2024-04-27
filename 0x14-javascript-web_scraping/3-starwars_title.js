#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

const endpoint =
  'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(endpoint, function (err, r, body) {
  if (!err && r.statusCode === 200) { console.log(JSON.parse(body).title); }
});
