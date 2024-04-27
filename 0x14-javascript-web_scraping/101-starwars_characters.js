#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const util = require('node:util');

const rp = util.promisify(request)

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function getCharacterName (urls, index) {
  if (!urls || index === urls.length) { return; }
  rp(urls[index])
		.then(data => data.body)
    .then((data) => JSON.parse(data))
    .then((characterInfo) => console.log(characterInfo.name))
    .then(() => getCharacterName(urls, ++index))
    .catch((err) => console.log(err.code));
}

async function getAllCharacters () {
  const characters = await rp(url)
		.then(data => data.body)
    .then((data) => JSON.parse(data).characters)
    .catch((err) => console.log('Not exists:'));
  getCharacterName(characters, 0);
}
getAllCharacters();
