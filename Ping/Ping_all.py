import os
import sys
import subprocess

# ANSI color codes
RED = "\033[1;97;41m"
GREEN = "\033[1;97;42m"
RESET = "\033[0;37m"
DIM = "\033[2m"

def ping_host(domain):
    try:
        result = subprocess.run(
            ["ping", "-c", "2", domain],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def main():
    if len(sys.argv) < 2:
        print(f"{RED} No target supplied {RESET}")
        return

    target_file = sys.argv[1]

    if not os.path.isfile(target_file):
        print(f"{RED} File '{target_file}' not found {RESET}")
        return

    print(f"{DIM}{RED} Make sure you have added new line in the ping file {RESET}")
    print("Initiating Ping...\n")

    with open(target_file, 'r') as f, open("Pingstatus.md", 'a') as out_file:
        for line in f:
            domain = line.strip()
            if not domain:
                continue

            if ping_host(domain):
                print(f"{GREEN} [+] Host [{domain}] is up {RESET}")
                out_file.write(domain + '\n')

if __name__ == "__main__":
    main()
