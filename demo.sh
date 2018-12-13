#!/bin/bash
docker stop $(docker ps -aq)
docker rm $(docker container ls -aq)
docker rmi -f $(docker images -aq)
# docker-compose up nginx

