import sys, os, subprocess

supported_commands = ["exit", "echo", "type", "pwd"]
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
        what_to_echo = " ".join(args)
        sys.stdout.write(f"{what_to_echo}\n")
    elif command == 'pwd':
        sys.stdout.write(f"{os.getcwd()}\n")
    elif command == 'cd':
        handle_cd_command(args)
    elif command == 'type':
        handle_type_command(paths, args[0])
    else:
        custom_command = get_custom_command_if_exists(command=command)

        if custom_command is None:
            sys.stdout.write(f"{command}: not found\n")
        else:
            result = subprocess.run([custom_command, *args], capture_output=True, text=True)
            sys.stdout.write(result.stdout)

def handle_cd_command(args: [str]):
    path = args[0]
    if path == '~':
        os.chdir(f"{os.path.expanduser(path)}")
    elif os.path.isdir(f"{path}"):
        os.chdir(f"{path}")
    else:
        sys.stdout.write(f"cd: {path}: No such file or directory\n")

def handle_type_command(paths: [str], target_command: str):
    command_path_key = None
    if len(paths) > 0:
        for path in paths:
            if os.path.isfile(f"{path}/{target_command}"):
                command_path_key = f"{path}/{target_command}"
    
    if target_command in supported_commands:
        sys.stdout.write(f"{target_command} is a shell builtin\n")
    elif command_path_key is not None:
        sys.stdout.write(f"{target_command} is {command_path_key}\n")
    else:
        sys.stdout.write(f"{target_command}: not found\n")

def get_custom_command_if_exists(command: str):
    paths = path_str.split(":")
    if len(paths) > 0:
        for path in paths:
            if os.path.isfile(f"{path}/{command}"):
                return f"{path}/{command}"
    return None

if __name__ == "__main__":
    main()
