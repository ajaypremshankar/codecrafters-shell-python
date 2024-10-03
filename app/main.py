import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        print(f"{command}: not found")


if __name__ == "__main__":
    main()
