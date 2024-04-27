#!/usr/bin/node

const { argv } = require('node:process');
const rp = require('request-promise');

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function getCharacterName (urls, index) {
  if (!urls || index === urls.length) { return; }
  rp(urls[index])
    .then((data) => JSON.parse(data))
    .then((characterInfo) => console.log(characterInfo.name))
    .then(() => getCharacterName(urls, ++index))
    .catch((err) => console.log(err));
}

async function getAllCharacters () {
  const characters = await rp(url)
    .then((data) => JSON.parse(data).characters)
    .catch((err) => console.log('Not exists:', err.options.uri));
  getCharacterName(characters, 0);
}
getAllCharacters();
