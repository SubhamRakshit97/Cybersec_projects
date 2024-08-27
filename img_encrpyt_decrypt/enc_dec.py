from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import io

# Encryption Function
def encrypt_image(image_path, key, output_path):
    # Load image and convert to bytes
    image = Image.open(image_path)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()
    
    # Generate AES cipher
    iv = os.urandom(16)  # AES block size is 16 bytes
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad and encrypt image bytes
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(image_bytes) + padder.finalize()
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()
    
    # Save encrypted data to file
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

# Decryption Function
def decrypt_image(encrypted_path, key, output_image_path):
    # Load encrypted data
    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()
    
    # Extract IV from the beginning of the encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Generate AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt and unpad data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    padded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Convert bytes back to image
    image = Image.open(io.BytesIO(padded_data))
    image.save(output_image_path)

# Main execution
if __name__ == "__main__":
    # Generate a random AES key
    key = os.urandom(32)  # AES-256 requires a 32-byte key

    # Encrypt the image
    encrypt_image('/Users/musubimanagement/Desktop/cyber/img_encrpyt_decrypt/img_cyber.webp', key, 'encrypted_image.bin')
    print("Image encrypted successfully!")

    # Decrypt the image
    decrypt_image('encrypted_image.bin', key, 'decrypted_image.png') #stored with decrypted_image.png name
    print("Image decrypted successfully!")

