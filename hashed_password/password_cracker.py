import hashlib
import itertools
import string

def hash_password(password, algorithm='md5'):
    """Hash a password using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm)
    return hash_func(password.encode()).hexdigest()

def brute_force_crack(hashed_password, algorithm='md5', max_length=4):
    """Attempt to crack the hashed password using brute-force."""
    characters = string.ascii_lowercase + string.digits  # Adjust character set as needed
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            if hash_password(guess_password, algorithm) == hashed_password:
                return guess_password
    return None

def dictionary_attack_crack(hashed_password, dictionary_file, algorithm='md5'):
    """Attempt to crack the hashed password using a dictionary attack."""
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            if hash_password(password, algorithm) == hashed_password:
                return password
    return None

def main():
    hashed_password = input("Enter the hashed password to crack: ").strip()
    attack_method = input("Choose attack method (brute-force/dictionary): ").strip().lower()
    
    algorithm = 'md5'  # You can change to 'sha1' or 'sha256' as needed
    if attack_method == 'brute-force':
        max_length = int(input("Enter maximum password length for brute-force attack: "))
        print(f"Cracking with brute-force (max length {max_length})...")
        cracked_password = brute_force_crack(hashed_password, algorithm, max_length)
        if cracked_password:
            print(f"Password found: {cracked_password}")
        else:
            print("Password not found.")
    elif attack_method == 'dictionary':
        dictionary_file = input("Enter the path to the dictionary file: ").strip()
        print("Cracking with dictionary attack...")
        cracked_password = dictionary_attack_crack(hashed_password, dictionary_file, algorithm)
        if cracked_password:
            print(f"Password found: {cracked_password}")
        else:
            print("Password not found.")
    else:
        print("Invalid attack method. Choose 'brute-force' or 'dictionary'.")

if __name__ == "__main__":
    main()

# MD5 Hash of password is: 5f4dcc3b5aa765d61d8327deb882cf99 