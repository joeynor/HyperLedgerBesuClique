# README for enode.sh

This is a simple shell script named `enode.sh` that is used to fetch the Ethereum node information from a local Ethereum node.

## Script Description

The script uses `curl` and `jq` to send a JSON-RPC request to the local Ethereum node and parse the response.

Here is the script:

```shellscript
curl -s -X POST --data '{"jsonrpc":"2.0","method":"admin_nodeInfo","params":[],"id":1}' http://127.0.0.1:8545 | jq -r '.result.enode'
```

## How it works

1. `curl -s -X POST --data '{"jsonrpc":"2.0","method":"admin_nodeInfo","params":[],"id":1}' http://127.0.0.1:8545` : This command sends a POST request to the local Ethereum node (running at `http://127.0.0.1:8545`). The `-s` option makes `curl` silent. The `--data` option is used to pass the JSON-RPC request data.

2. `| jq -r '.result.enode'` : This command takes the output of the `curl` command and pipes it to `jq`, a command-line JSON processor. The `-r` option tells `jq` to output raw strings instead of JSON-encoded strings. The `.result.enode` is a filter that extracts the `enode` field from the `result` field of the JSON response.

## Requirements

To run this script, you need to have `curl` and `jq` installed on your system. Also, you need to have a local Ethereum node running at `http://127.0.0.1:8545`.

## Usage

To use this script, simply run it from the command line:

```shellscript
bash enode.sh
```

This will print the `enode` information of your local Ethereum node to the console.
