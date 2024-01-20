# Active File Runner

This script is used to manage and run containers for a specific application. It provides a way to set up the environment, start and stop containers, and perform other related tasks.

## Environment Variables

The script uses several environment variables:

- `EXPLORER`: If not provided, it defaults to `false`.
- `PORT`: The port on which the application will run. If not provided, it defaults to `9600`.
- `ALLOC`: If provided and greater than `0`, the `alloc` function will be called.
- `BASE`: The base directory for the application. If not provided, it defaults to the current working directory.
- `BALANCE`: If not provided, it defaults to `90000000000000000000000`.

## Actions

The script can perform several actions based on the `ACTION` environment variable:

- `start`: Starts the containers by calling the `run_containers` function.
- `stop`: Stops the containers by calling the `stop_containers` function.
- `silent`: Does nothing.
- If no valid action is provided, the `show_help` function is called to display usage information.

## Initialization

If the `INIT` environment variable is set to `true`, the `innit` function is called.

## Usage

To use this script, set the appropriate environment variables and then run the script with the desired action. For example:

```shellscript
export ACTION=start
export PORT=9600
./runner
```

This will start the containers on port `9600`.
