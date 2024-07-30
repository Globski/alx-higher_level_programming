#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(character => {
      request(character, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const charData = JSON.parse(charBody);
          console.log(charData.name);
        }
      });
    });
  }
});
