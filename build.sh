#!/bin/bash

# build besu image
cd containers/Genesis && docker build -t genesis-v2 .

# build image for nodes
cd ../Nodes && docker build -t node-v2 .

# run compose file for all besu network
cd ../ && docker-compose up -d

# run compose file for explorer
cd chainlens-free/docker-compose && NODE_ENDPOINT=http://172.16.239.1:8545 docker-compose up --force-recreate -d | tee chainlens.log