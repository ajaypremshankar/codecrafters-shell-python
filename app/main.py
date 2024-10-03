import sys, os

supported_commands = ["exit", "echo", "type"]
path_str = os.environ.get("PATH")
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        command_and_params = command.split(" ")

        command_key = command_and_params[0]
        paths = path_str.split(":") if path_str  else [] 
        args = command_and_params[1:]

        handle_command(paths=paths, command=command_key, args=args)

def handle_command(paths: [str], command: str, args: [str]):
    if command == 'exit':
        sys.exit(int(args[0]))
    elif command == 'echo':
        print(" ".join(args))
    elif command == 'type':
        handle_type_command(paths, args[0])
    else:
        print(f"{command}: not found")


def handle_type_command(paths: [str], target_command: str):
    command_path_key = None
    if len(paths) > 0:
        for path in paths:
            if os.path.isfile(f"{path}/{target_command}"):
                command_path_key = f"{path}/{target_command}"
    
    if target_command in supported_commands:
        print(f"{target_command} is a shell builtin")
    elif command_path_key is not None:
        print(f"{target_command} is {command_path_key}")
    else:
        print(f"{target_command}: not found")

def has_path(command: str):
    return True if command.startswith("PATH=") else False

def get_paths(path: str):
    paths_str = path.split("=")[1]
    return paths_str.split(":")


if __name__ == "__main__":
    main()
