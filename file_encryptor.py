from cryptography.fernet import Fernet
from termcolor import colored
import os

# Banner
def banner():
    print(colored("""
########################################
#       Cyber Gita Company             #
#       File Encryptor/Decryptor       #
########################################
""", 'cyan'))

# Generate key
def generate_key():
    return Fernet.generate_key()

# Encrypt file
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(file_path + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        print(colored(f"[+] File encrypted: {file_path}.enc", 'green'))
    except Exception as e:
        print(colored(f"[-] Error: {e}", 'red'))

# Decrypt file
def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path[:-4], 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(colored(f"[+] File decrypted: {file_path[:-4]}", 'green'))
    except Exception as e:
        print(colored(f"[-] Error: {e}", 'red'))

if __name__ == "__main__":
    banner()
    key = generate_key()
    print(colored(f"[+] Your encryption key: {key.decode()}", 'yellow'))
    choice = input(colored("[+] Enter 'e' to encrypt or 'd' to decrypt: ", 'yellow'))
    file_path = input(colored("[+] Enter the file path: ", 'yellow'))
    if choice == 'e':
        encrypt_file(file_path, key)
    elif choice == 'd':
        decrypt_file(file_path, key)
    else:
        print(colored("[-] Invalid choice!", 'red'))
