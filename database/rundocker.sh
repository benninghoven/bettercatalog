#!/bin/bash

# must be lowercase!
NAME="bettercatalog_database"

IMAGE=$NAME"_image"
CONTAINER=$NAME"_container"

found=$(docker images -q $IMAGE)

# if image is not found
if [ -z "$found" ]; then
  echo "🐳 Image not found, creating..."
  docker build -t $IMAGE .
else
  echo "🐳 Image found"
fi

docker run -it \
    -p 3306:3306 \
    --name $CONTAINER \
    $IMAGE

# auto delete container after it ran
docker rm $CONTAINER
