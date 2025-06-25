#  FastAPI Docker Project
This project is a containerized web API built using FastAPI and served via Docker. 

## App Design Overview

- FastAPI handles all routing, logic, and automatic OpenAPI documentation
- Dockerfile builds a portable image using Python and installs dependencies
- Docker Compose*maps port `8080` and simplifies running the service

##  Files - Struture

`main.py` | Defines the FastAPI app and its routes 
`requirements.txt` | Lists required Python packages (`fastapi`, `uvicorn`, etc.) 
`Dockerfile` | Instructions to build the Docker image 
`docker-compose.yaml` | Runs the app in a container and maps port `8080` 
`runner.sh` | Optional script to build and launch the app using Compose 


## How to run
# Build image
docker build -t fastapi-app .
# Run container
docker run -d -p 8080:8080 --name fastapi-container fastapi-app
Note: You can also run it through the DOCKER Desktop app - make sure you specify port explicitly before you run it. 

# Open in browser
# http://localhost:8080 or http://localhost:8080/docs

