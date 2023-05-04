#!/bin/bash

# must be lowercase!
NAME="bettercatalog_frontend"

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

docker run -it --rm \
    -p 80:80 \
    --name $CONTAINER \
    --network my_network \
    --network-alias frontend \
    $IMAGE

# auto delete container after it ran
docker rm $CONTAINER
