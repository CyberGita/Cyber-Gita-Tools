import os
import subprocess
from termcolor import colored

# Banner
def banner():
    print(colored("""
########################################
#       Cyber Gita Company             #
#       Network Scanner Tool          #
########################################
""", 'cyan'))

# Scan network
def scan_network():
    banner()
    print(colored("[+] Scanning network...", 'yellow'))
    try:
        # Run nmap command
        result = subprocess.run(['nmap', '-sP', '192.168.1.0/24'], capture_output=True, text=True)
        print(colored(result.stdout, 'green'))
    except Exception as e:
        print(colored(f"[-] Error: {e}", 'red'))

if __name__ == "__main__":
    scan_network()
