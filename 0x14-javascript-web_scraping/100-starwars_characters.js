#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

async function getCharacterName (url) {
  await request.get(url, function (err, r, body) {
    if (!err && r.statusCode === 200) {
      console.log(JSON.parse(body).name);
    } else {
      console.log(err.message);
    }
  });
}

async function getAllCharachters () {
  await request(url, function (err, r, body) {
    if (!err && r.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      characters.forEach(character => {
        getCharacterName(character);
      });
    } else {
      console.log(err.message);
    }
  });
}
getAllCharachters();
