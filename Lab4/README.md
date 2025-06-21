This project runs a FastAPI app inside a Docker container and shows it on port 8080.
This is how you can build it adn run it. 

# Build image
docker build -t fastapi-app .

# Run container
docker run -d -p 8080:8080 --name fastapi-container fastapi-app
Note: You can also run it through the DOCKER Desktop app - make sure you specify port explicitly before you run it. 

# Open in browser
# http://localhost:8080 or http://localhost:8080/docs

