import subprocess
import sys

def ping(domain):
    try:
        # Run ping and capture both stdout and stderr
        result = subprocess.run(
            ["ping", "-n", "2", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error pinging {domain}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bulk_ping.py domains.txt")
        return

    target_file = sys.argv[1]

    try:
        with open(target_file, 'r') as f, open("Pingstatus.md", 'a') as out:
            for line in f:
                domain = line.strip()
                if not domain:
                    continue

                is_up = ping(domain)

                if is_up:
                    print(f"[+] Host {domain} is up")
                    out.write(f"{domain}\n")
                else:
                    print(f"[-] Host {domain} is down or unreachable")
    except FileNotFoundError:
        print(f"File '{target_file}' not found.")

if __name__ == "__main__":
    main()
