import json
import argparse
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware, construct_sign_and_send_raw_middleware
from eth_account import Account


def load_private_keys_from_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            private_keys = json.load(file)["private_keys"]
            return private_keys
    except FileNotFoundError:
        print("File not found. Using backup keys.json file.")
        with open("../containers/data/keys/accounts/keys.json", "r") as file:
            private_keys = json.load(file)["private_keys"]
        return private_keys


def initialize_accounts(private_keys: list) -> list:
    return [Account.from_key(private_key) for private_key in private_keys]


def initialize_middleware(accounts: list) -> None:
    for account in accounts:
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))


def get_balance(account: Account) -> int:
    return w3.eth.get_balance(account.address)


def send_transaction(sender: Account, receiver: Account, amount: int) -> str:
    tx = {
        "from": sender.address,
        "to": receiver.address,
        "value": amount,
        "gas": 2000000,
        "gasPrice": w3.to_wei("50", "gwei"),
        "nonce": w3.eth.get_transaction_count(sender.address),
    }
    tx_hash = w3.eth.send_transaction(tx)
    return tx_hash.hex()


def list_accounts(accounts: list) -> None:
    for i, account in enumerate(accounts):
        print(f"Account {i + 1}:")
        print(f"Address: {account.address}")
        print(f"Balance: {get_balance(account)} wei\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Manage Ethereum accounts and transactions."
    )
    parser.add_argument(
        "--keystore",
        type=str,
        default="keys.json",
        help="Path to the keystore file.",
    )
    parser.add_argument(
        "action",
        choices=["get_accounts", "send_transaction", "view_account"],
        help="Action to perform.",
    )
    parser.add_argument(
        "--host", type=str, default="http://127.0.0.1:8545", help="Ethereum node host."
    )

    args = parser.parse_args()

    w3 = Web3(HTTPProvider(args.host))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    private_keys = load_private_keys_from_file(args.keystore)
    accounts = initialize_accounts(private_keys)
    initialize_middleware(accounts)

    if args.action == "get_accounts":
        list_accounts(accounts)
    elif args.action == "send_transaction":
        sender_index = int(input("Enter sender account index: ")) - 1
        receiver_index = int(input("Enter receiver account index: ")) - 1
        amount = w3.to_wei(input("Enter amount in ether: "), "ether")
        transaction_hash = send_transaction(
            accounts[sender_index], accounts[receiver_index], amount
        )
        print(f"Transaction sent. \nTransaction hash: {transaction_hash}")
    elif args.action == "view_account":
        account_index = int(input("Enter account index: ")) - 1
        account = accounts[account_index]
        print(f"Account {account_index + 1} details:")
        print(f"Address: {account.address}")
        print(f"Balance: {get_balance(account)} wei")
    else:
        print(
            "Invalid action. Please choose from 'get_accounts', 'send_transaction', or 'view_account'."
        )
