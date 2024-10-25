import hashlib
import os
import time
import re
import subprocess

# Define supported hash types
hash_types = {
    'md5': {'length': 32, 'pattern': r'^[a-fA-F0-9]{32}$'},
    'sha1': {'length': 40, 'pattern': r'^[a-fA-F0-9]{40}$'},
    'sha224': {'length': 56, 'pattern': r'^[a-fA-F0-9]{56}$'},
    'sha256': {'length': 64, 'pattern': r'^[a-fA-F0-9]{64}$'},
    'sha384': {'length': 96, 'pattern': r'^[a-fA-F0-9]{96}$'},
    'sha512': {'length': 128, 'pattern': r'^[a-fA-F0-9]{128}$'},
    'blake2b': {'length': 64, 'pattern': r'^[a-fA-F0-9]{64}$'},
    'blake2s': {'length': 32, 'pattern': r'^[a-fA-F0-9]{32}$'},
}

def identify_hash_type(hash_value):
    """Identify the type of a given hash."""
    for hash_type, properties in hash_types.items():
        if len(hash_value) == properties['length'] and re.match(properties['pattern'], hash_value):
            return hash_type
    return "Unknown hash type"

def hash_identifier():
    """Function to prompt user for a hash and identify its type."""
    while True:
        user_hash = input("Enter the hash value to identify -> ").strip()
        if user_hash:
            hash_type = identify_hash_type(user_hash)
            if hash_type != "Unknown hash type":
                print(f"The identified hash type is: {hash_type}")
            else:
                print("Invalid hash value or unsupported hash type. Please try again.")
        else:
            print("Hash input cannot be empty. Please try again.")
        retry = input("Do you want to try another hash? (y/n) -> ").strip().lower()
        if retry != 'y':
            break

def generate_custom_wordlist():
    """Function to call the WLgenerator.py script."""
    # Call the WLgenerator.py script using subprocess
    try:
        subprocess.run(["python", "WLgenerator.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating wordlist: {e}")

# Function to crack the password
def pass_crack(hashed_pass, hash_type, wordlist_path="rockyou.txt"):
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.isfile(wordlist_path):
        print(f"Wordlist file '{wordlist_path}' not found.")
        return None

    print(f"Trying to crack {hashed_pass} using {hash_type} hash...")

    # Supported hash methods
    hash_methods = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s
    }

    hash_method = hash_methods.get(hash_type)
    if hash_method is None:
        print("Unsupported hash type.")
        return None

    print(f"Using wordlist: {wordlist_path}")

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [password.strip() for password in f]

    for password in passwords:
        hashed_word = hash_method(password.encode()).hexdigest()
        if hashed_word == hashed_pass:
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Cracked!!!\n\nPassword is: {password}")
            return password

    print("Password not found in the wordlist.")
    return None

# Main function to run the password cracker
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Ask if the user wants to identify a hash
    identify_hash = input("Do you want to identify a hash? (y/n) -> ").strip().lower()
    if identify_hash == 'y':
        hash_identifier()
    
    input("\nPress Enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')

    # Ask if the user wants to create a custom wordlist
    create_custom_wordlist_choice = input("Do you want to create a custom wordlist? (y/n) -> ").strip().lower()
    if create_custom_wordlist_choice == 'y':
        generate_custom_wordlist()
    input("\nPress Enter to continue...")
    
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get the hashed password from the user
    while True:
        hashed_password = input("Enter the hashed password -> ").strip()
        if hashed_password:
            break
        else:
            print("Hashed password cannot be empty. Please try again.")

    # Get the hash type from the user
    while True:
        hash_type = input("Enter the hash type -> ").strip().lower()
        if hash_type in hash_types:
            break
        else:
            print(f"Unsupported or unknown hash type '{hash_type}'. Please enter a valid hash type (e.g., md5, sha1, sha256).")

    # Ask if the user wants to provide a custom wordlist
    custom_wordlist = input("Do you want to upload a custom wordlist? (y/n) -> ").strip().lower()
    if custom_wordlist == 'y':
        while True:
            wordlist_path = input("Enter the path to the custom wordlist -> ").strip()
            if os.path.isfile(wordlist_path):
                break
            else:
                print("Invalid file path. Please enter a valid path to a wordlist.")
    else:
        wordlist_path = os.path.join(os.path.dirname(__file__), 'rockyou.txt')

    pass_crack(hashed_password, hash_type, wordlist_path)

if __name__ == "__main__":
    main()
