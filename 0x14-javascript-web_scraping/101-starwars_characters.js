#!/usr/bin/env node

const request = require('request');

if (process.argv.length < 3) {
    console.log("Usage: ./101-starwars_characters.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to retrieve film with ID ${movieId}`);
        return;
    }

    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error:', charError);
                return;
            }

            if (charResponse.statusCode === 200) {
                const character = JSON.parse(charBody);
                console.log(character.name);
            } else {
                console.error(`Failed to retrieve character from ${characterUrl}`);
            }
        });
    });
});
