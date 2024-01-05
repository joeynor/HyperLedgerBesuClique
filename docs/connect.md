# README for connector.py

This is a Python script named `connector.py` that is used to manage Ethereum accounts and transactions.

## Script Description

The script uses the `web3.py` library to interact with the Ethereum blockchain. It provides functionalities to list accounts, send transactions, and view account details.

## How it works

The script takes command-line arguments to perform different actions:

1. `--keystore`: Path to the keystore file. Default is `keys.json`.
2. `action`: The action to perform. Choices are `get_accounts`, `send_transaction`, and `view_account`.
3. `--host`: Ethereum node host. Default is `http://127.0.0.1:8545`.

The script initializes a `Web3` instance with the provided host, loads private keys from the keystore file, and initializes accounts and middleware.

Depending on the `action` argument, the script performs different actions:

- `get_accounts`: Lists all accounts.
- `send_transaction`: Asks for sender and receiver account indices and the amount in ether, sends a transaction, and prints the transaction hash.
- `view_account`: Asks for an account index and prints the account details.

## Requirements

To run this script, you need to have Python 3 and the `web3.py` library installed on your system. Also, you need to have an Ethereum node running at the host provided by the `--host` argument.

## Usage

To use this script, run it from the command line with the desired arguments. For example:

```shell
python connector.py --keystore mykeys.json get_accounts
```

This will list all accounts using the private keys from the `mykeys.json` file.
