def encrypt(text, shift):
    """Encrypts the text using the Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift the character within its case (upper or lower)
            shift_amount = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            encrypted_text += encrypted_char
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    """Decrypts the text using the Caesar Cipher."""
    return encrypt(ciphertext, -shift)

# User input
text = input("Enter the text to encrypt: ")

while True:
    try:
        shift = int(input("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Please enter a number between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Encryption
encrypted_text = encrypt(text, shift)
print(f"Encrypted Text: {encrypted_text}")

# Decryption
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted Text: {decrypted_text}")

