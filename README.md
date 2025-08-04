# powerplant-coding-challenge

## Setting up environment

1. Install Docker on machine

## Build and run API

1. Build image with command (need to be on root project level): docker build -t powerplant-api .

2. Run container with command (don't forget to stop container!!!): docker run -d -p 8888:8888 --name powerplant-fastapi  powerplant-api

## Swagger

Go to url: http://localhost:8888/docs
