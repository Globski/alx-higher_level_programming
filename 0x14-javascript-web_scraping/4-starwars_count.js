#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const count = data.results.filter(film =>
      film.characters.find(character => character.endsWith('/18/'))
    ).length;
    console.log(count);
  }
});
