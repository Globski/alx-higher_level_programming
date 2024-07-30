#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characterRequests = data.characters.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(characterRequests)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  }
});
