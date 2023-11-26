#!/bin/bash

declare -r TIMEOUT=5
declare enode0=""
declare enode1=""

while [ -z "$enode0" ] || [ -z "$enode1" ]; do
    enode0=$(curl -s -X POST --data '{"jsonrpc":"2.0","method":"admin_nodeInfo","params":[],"id":1}' http://127.0.0.1:8555 | jq -r '.result.enode')
    enode1=$(cat /opt/besu/data/genesis_enode)
    
    if [ -z "$enode0" ] || [ -z "$enode1" ]; then
        echo "Enodes are empty. Sleeping for $TIMEOUT seconds and retrying..."
        sleep $TIMEOUT
    fi
done

# Both enode0 and enode1 have values
echo "Enode0: $enode0"
echo "Enode1: $enode1"

# Run Besu command with --bootnodes
/opt/besu/bin/besu --bootnodes="$enode1","$enode0" "$@"
