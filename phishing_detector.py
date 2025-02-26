import requests
from termcolor import colored

# Banner
def banner():
    print(colored("""
########################################
#       Cyber Gita Company             #
#       Phishing URL Detector          #
########################################
""", 'cyan'))

# Check URL
def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colored(f"[+] URL is accessible: {url}", 'green'))
            # Add more checks here (e.g., domain age, SSL certificate)
        else:
            print(colored(f"[-] URL is not accessible: {url}", 'red'))
    except Exception as e:
        print(colored(f"[-] Error: {e}", 'red'))

if __name__ == "__main__":
    banner()
    url = input(colored("[+] Enter the URL to check: ", 'yellow'))
    check_url(url)
