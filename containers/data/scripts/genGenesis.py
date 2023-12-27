#!/bin/env python3

import json
import os


class ExtraData:
    def __init__(self, genesis_template_file: str) -> None:
        self.genesis_file = genesis_template_file
        self.genesis = None
        self.keys: str = ""
        self._generate()

    def _generate(self) -> None:
        with open(self.genesis_file, "r") as f:
            self.genesis = json.load(f)

        # open the folder keys, and get all the files
        keys = os.listdir("../keys")

        # for each file, get the address and add it to the extra data
        for key in keys:
            with open("../keys/" + key, "r") as f:
                address = f.read()[2:]
                self.keys += address

    def __str__(self) -> str:
        return str(self.genesis["extraData"]).replace("_", self.keys)

    def create_new_genesis_file(self, genesis_file: str) -> None:
        self.genesis["extraData"] = str(self.genesis["extraData"]).replace(
            "_", self.keys
        )
        with open(genesis_file, "w") as f:
            json.dump(self.genesis, f, indent=4)


if __name__ == "__main__":
    genesis_template_file = "../cliqueGenesisTemplate.json"
    extraData = ExtraData(genesis_template_file=genesis_template_file)
    extraData.create_new_genesis_file("../cliqueGenesis.json")
