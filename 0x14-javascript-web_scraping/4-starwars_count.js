#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const endpoint = argv[2];
request(endpoint, function (err, r, body) {
  let films;

  if (!err && r.statusCode === 200) { films = JSON.parse(body).results; }
  films = films.filter(f =>
    f.characters.filter(
      c => c.endsWith('18/')).length
  );
  console.log(films.length);
});
