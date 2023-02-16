#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from the command line argument
const movieId = process.argv[2];

// Make a GET request to the Star Wars API to retrieve the movie information
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }

  // Parse the movie information from the response body
  const movie = JSON.parse(body);

  // Loop through the list of character URLs and make a GET request for each one
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error making request:', error);
        return;
      }

      // Parse the character information from the response body
      const character = JSON.parse(body);

      // Print the character name
      console.log(character.name);
    });
  });
});
