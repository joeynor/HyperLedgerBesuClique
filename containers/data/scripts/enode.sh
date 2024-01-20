#!/bin/bash

declare -r TIMEOUT=5
declare ENODE0=""

while [ -z "$ENODE0" ]; do
    ENODE0=$(curl -s -X POST --data '{"jsonrpc":"2.0","method":"admin_nodeInfo","params":[],"id":1}' http://127.0.0.1:8545 | jq -r '.result.enode')
    
    if [ -z "$ENODE0" ] || [ -z "${ENODE0+x}" ] || [ "$ENODE0" = "null" ]; then
        echo "Enode is either empty or null. Sleeping for $TIMEOUT seconds and retrying..."
        sleep $TIMEOUT
    else
        # Save ENODE0 to a file
        echo "$ENODE0" > /opt/besu/data/genesis_enode
        
        # Run Besu command with --bootnodes
        /opt/besu/bin/besu --bootnodes="$ENODE0" "$@"
        echo "Enode is $ENODE0"
    fi
done

