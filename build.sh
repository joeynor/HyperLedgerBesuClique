#!/bin/bash

# install python dependencies
cd connect && pip3 install -r requirements.txt

# build besu image
cd ../containers/Genesis && docker build -t genesis-v2 .

# build image for nodes
cd ../Nodes && docker build -t node-v2 .

# run compose file for all besu network
cd ../ && docker-compose up -d

# determine the operating system
case "$(uname -s)" in
    Linux*)     # Linux
        cd chainlens-free/docker-compose && NODE_ENDPOINT=http://172.16.239.1:8545 docker-compose up --force-recreate -d
    ;;
    Darwin*)    # macOS
        cd chainlens-free/docker-compose && NODE_ENDPOINT=http://host.docker.internal:8545 docker-compose up --force-recreate -d
    ;;
    CYGWIN*)    # Windows
        cd chainlens-free/docker-compose &&  NODE_ENDPOINT=http://host.docker.internal:8545 docker-compose up --force-recreate -d
    ;;
    MINGW*)     # Windows
        cd chainlens-free/docker-compose &&  NODE_ENDPOINT=http://host.docker.internal:8545 docker-compose up --force-recreate -d
    ;;
    *)
        echo "Unsupported operating system"
        exit 1
    ;;
esac
