#!/bin/bash

docker build -t flask-blog .
docker run --rm -p 5000:5000 --name flaskblog-ap flask-blog