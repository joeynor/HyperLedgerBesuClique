#!/bin/env python3

import json
import os


class ExtraData:
    def __init__(self, genesis_template_file: str, balance, **kwargs) -> None:
        self.genesis_template_file = genesis_template_file
        self.genesis = None
        self.keys: str = ""
        self.balance = balance
        self.keystore_file = kwargs.get("keystore_file", None)
        self.override_genesis = kwargs.get("override_genesis", False)
        self.alloc = kwargs.get("alloc", "False")
        self._generate()

    def _generate(self) -> None:
        with open(self.genesis_template_file, "r") as f:
            self.genesis = json.load(f)

        # open the folder keys, and get all the files
        keys = os.listdir("../keys/nodes")

        # for each file, get the address and add it to the extra data
        for key in keys:
            with open("../keys/nodes/" + key, "r") as f:
                address = f.read()[2:]
                self.keys += address

        self.genesis["extraData"] = str(self.genesis["extraData"]).replace(
            "_", self.keys
        )

    def __str__(self) -> str:
        return str(self.genesis["extraData"]).replace("_", self.keys)

    def create_new_genesis_file(self, genesis_file: str) -> None:
        # open over the folder accounts, and loop over all the accounts from 0..x and create alloc field using the content of file key.pem
        if "True" or "true" in self.alloc:
            accounts = []
            private_keys = []
            for account in os.listdir("../keys/accounts"):
                try:
                    with open("../keys/accounts/" + account + "/key.pub", "r") as f:
                        address = f.read()[2:]
                        accounts.append({address: {"balance": self.balance}})

                    with open("../keys/accounts/" + account + "/key", "r") as f:
                        private_keys.append(f.read())
                except FileNotFoundError:
                    print("File not found. Run runner with --alloc to generate keys.")
                except NotADirectoryError:
                    ...

            with open(self.keystore_file, "w") as f:
                private_keys = {"private_keys": private_keys}
                json.dump(private_keys, f, indent=4)

            first_format = {"alloc": {}}

            for account_info in accounts:
                address, details = account_info.popitem()
                first_format["alloc"][address] = {"balance": details["balance"]}
            self.genesis["alloc"] = first_format["alloc"]

        if "True" or "true" in self.override_genesis:
            with open(genesis_file, "w") as f:
                json.dump(self.genesis, f, indent=4)


if __name__ == "__main__":
    # parse arg with --account-balance

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--account-balance",
        default=90000000000000000000000,
    )
    parser.add_argument(
        "--genesis-template-file",
        type=str,
        default="../cliqueGenesisTemplate.json",
    )
    parser.add_argument(
        "--genesis-file",
        help="Path to where the genesis file should be saved.",
        type=str,
        default="../cliqueGenesis.json",
    )
    parser.add_argument(
        "--keystore-file",
        help="Path to where the keystore file should be saved.",
        type=str,
        default="../keys/accounts/keys.json",
    )
    parser.add_argument(
        "--override-genesis",
        help="Override the genesis file.",
        default="False",
    )
    parser.add_argument(
        "--alloc",
        help="save alloc or not.",
        default="False",
    )

    args = parser.parse_args()
    extraData = ExtraData(
        genesis_template_file=args.genesis_template_file,
        balance=args.account_balance,
        override_genesis=args.override_genesis,
        genesis_file=args.genesis_file,
        keystore_file=args.keystore_file,
        alloc=args.alloc,
    )

extraData.create_new_genesis_file(genesis_file=args.genesis_file)
