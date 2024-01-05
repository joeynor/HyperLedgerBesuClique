# genGenesis Python Script

This Python script is used to generate a genesis file for a blockchain network. It reads a template genesis file, modifies it based on the provided parameters, and writes the new genesis file to disk.

## Class: genGenesis

The `genGenesis` class is the main class in this script. It is responsible for generating the new genesis file.

### Methods

- `__init__`: Initializes a new instance of the `genGenesis` class. It takes a genesis template file and a balance as parameters, along with optional keyword arguments for the keystore file, whether to override the genesis file, and whether to save the allocation.

- `_generate`: This private method is called during initialization. It opens the genesis template file and loads it into memory. It then reads the keys from the `../keys/nodes` directory and adds them to the genesis data.

- `__str__`: Returns a string representation of the `genGenesis` instance. This is the `extraData` field from the genesis data, with underscores replaced by the keys.

- `create_new_genesis_file`: This method creates the new genesis file. It reads the accounts from the `../keys/accounts` directory, creates the `alloc` field for each account using the content of the `key.pub` file, and writes the private keys to the keystore file. If the `override_genesis` attribute is set to `True`, it also writes the new genesis data to the genesis file.

## Dependencies

This script requires Python 3 and uses the `json` and `os` modules from the Python Standard Library.

## Usage

This script is intended to be used as a module in a larger application. To use it, import the `genGenesis` class and create a new instance, passing the necessary parameters to the constructor. Then, call the `create_new_genesis_file` method to create the new genesis file.
