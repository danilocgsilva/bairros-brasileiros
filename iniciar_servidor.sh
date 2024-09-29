#!/bin/bash

container_servidor=$(docker ps | grep -i bairros_brasileiros_python | awk '{print $1}')

docker exec -it $container_servidor flask run --host=0.0.0.0
