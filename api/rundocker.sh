#!/bin/bash

# must be lowercase!
NAME="bettercatalog_api"

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
    -p 5000:5000 \
    --name $CONTAINER \
    --network my_network \
    --network-alias api \
    $IMAGE

# auto delete container after it ran
docker rm $CONTAINER
