#!/bin/bash

IMAGE="bettercatalog_image"
CONTAINER="bettercatalog_container"

found=$(docker images -q $IMAGE)

# if image is not found
if [ -z "$found" ]; then
  echo "Image not found, creating..."
  docker build -t $IMAGE .
else
  echo "Image found"
fi

docker run -it \
    --mount type=bind,source="$(pwd)"/,target=/app \
    --name $CONTAINER \
    $IMAGE

# auto delete container after it ran
docker rm $CONTAINER
