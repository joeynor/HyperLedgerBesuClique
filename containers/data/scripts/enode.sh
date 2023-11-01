#!/bin/bash


sleep 5s # this is quite annoying

GENESIS_ENODE=$(curl -s -X POST --data '{"jsonrpc":"2.0","method":"admin_nodeInfo","params":[],"id":1}' http://127.0.0.1:8545 | jq -r '.result.enode')

echo $GENESIS_ENODE > /opt/besu/data/genesis_enode

/opt/besu/bin/besu --bootnodes=$GENESIS_ENODE $@
