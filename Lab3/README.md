# Lab3-CloudComputing
Welcome to the Harry Potter World!
In this project, you can get information about HP houses - exact same thing but using express this time not FastAPI. You can learn about their head teachers, founders, mascots and the colors. I have 11 routes, including simple, path, query and post.
This will be running on localhost port 8080. To run this, clone the whole repo - "git clone url". It is expected that you clone the repo using pycharm terminal. If using another IDE, things may be different. Then make sure you have express installed. 
After all,  run this command: "Lab3/routes.js". Then go to localhost:8080 to verify. To test POST, use this: " curl -X POST http://localhost:80
80/welcome -H "Content-Type: application/json" -d '{"name":"Harry","house":"Gryffindor"}'". To test header, use this: "curl -H "house: Hufflepuff" http://localhost:8080/verify-house"