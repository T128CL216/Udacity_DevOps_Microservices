#!/usr/bin/env bash

# Build Image
docker build --tag=api .

# List docker Images
docker image ls

#Run flask app
docker run -p 8000:5001 api