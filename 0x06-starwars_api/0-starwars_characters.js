#!/usr/bin/node

const request = require('request');
const async = require('async');

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

  // Create an array of functions to make a GET request for each character URL
  const characterRequests = movie.characters.map(characterUrl => {
    return function(callback) {
      request(characterUrl, (error, response, body) => {
        if (error) {
          callback(error);
          return;
        }

        // Parse the character information from the response body
        const character = JSON.parse(body);

        // Call the callback function with the character name
        callback(null, character.name);
      });
    };
  });

  // Use the async library to make the requests in parallel
  async.parallel(characterRequests, (error, characterNames) => {
    if (error) {
      console.error('Error making requests:', error);
      return;
    }

    // Print the list of character names
    console.log(characterNames.join('\n'));
  });
});
