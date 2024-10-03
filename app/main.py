import sys

supported_commands = ["exit", "echo", "type"]

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        command_and_params = command.split(" ")

        if command_and_params[0] in supported_commands:
            handle_command(command_and_params[0], command_and_params[1:])
        else:
            print(f"{command}: not found")


def handle_command(command: str, args: [str]):
    if command == 'exit':
        sys.exit(int(args[0]))
    elif command == 'echo':
        print(" ".join(args))
    elif command == 'type':
        if args[0] in supported_commands:
            print(f"{args[0]} is a shell builtin")
        else:
            print(f"{args[0]}: not found")


if __name__ == "__main__":
    main()
