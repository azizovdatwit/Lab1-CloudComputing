# Lab3-CloudComputing
Welcome to the Harry Potter World!

## Description
The app allows users to:

- View Hogwarts houses and their founders, mascots, and heads
- Use a playful Sorting Hat endpoint
- Get custom messages using query parameters
- Use headers to verify house identity
- Submit data via POST request for a welcome message

## Design & Structure
The project is a single-file Node.js application using the Express.js framework.
Main file is route.js. All houses info is hardcoded into JS object called "houses"


## Steps to run the server: 
To run this, clone the whole repo - "git clone url". It is expected that you clone the repo using pycharm terminal. If using another IDE, things may be different. Then make sure you have express installed.
1. cd Lab3 on Terminal
2. run "node routes.js"
3. click on localhost:8080 link on terminal

## Try in Browser
Use the following links after running the server:
Welcome Message → http://localhost:8080/
List of Houses → http://localhost:8080/houses
House Details → http://localhost:8080/house?name=gryffindor
Head of House → http://localhost:8080/house/head?name=slytherin
Mascot of House → http://localhost:8080/house/mascot?name=hufflepuff
Sorting Hat → http://localhost:8080/sortingHat?student=Harry
Learn a Spell → http://localhost:8080/spells?spell=lumos
Best Character → http://localhost:8080/bestCharacter?name=Hermione

To test POST, use this: " curl -X POST http://localhost:80
80/welcome -H "Content-Type: application/json" -d '{"name":"Harry","house":"Gryffindor"}'". To test header, use this: "curl -H "house: Hufflepuff" http://localhost:8080/verify-house"

