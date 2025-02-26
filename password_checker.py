import re
from termcolor import colored

# Banner
def banner():
    print(colored("""
########################################
#       Cyber Gita Company             #
#       Password Strength Checker      #
########################################
""", 'cyan'))

# Check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    return strength

if __name__ == "__main__":
    banner()
    password = input(colored("[+] Enter your password: ", 'yellow'))
    strength = check_password_strength(password)
    if strength == 5:
        print(colored("[+] Password is very strong!", 'green'))
    elif strength >= 3:
        print(colored("[+] Password is strong.", 'blue'))
    else:
        print(colored("[-] Password is weak!", 'red'))
