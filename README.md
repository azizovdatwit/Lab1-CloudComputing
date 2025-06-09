# Lab1-CloudComputing
Welcome to the Harry Potter World!
In this project, you can get information about HP houses. You can learn about their head teachers, founders, mascots and the colors. I have 11 routes, including simple, path, query and post.
Since this project uses fastAPI & uvicorn as app server, this will be running on localhost port 8080. To run this, clone the whole repo - "git clone url". It is expected that you clone the repo using pycharm terminal. If using another IDE, things may be different. Then make sure you have fastAPI installed, if not do "pip install fastapi". Same thing with uvicorn - "pip install uvicorn". 
After all,  run this command: "uvicorn main:app --port 8080 --reload". Then go to localhost:8080 to verify.

Lab2: In Lab2 folder, we implemented Python command line driver where it gives users 12 options to choose from and provide the information needed based on user selection - Lab2/main.py. Also, added 2 new routes: header and cookie routes. All these routes have also unittests which is testApi.py file.To run the tests, need to run this command on terminal: "python3 -m unittest {path to unittest file}"

Note: to run the code, make sure you are in the directory of your main.py file