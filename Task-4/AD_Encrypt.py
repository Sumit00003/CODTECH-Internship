import argparse
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag
import base64
import secrets

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a secure key from the password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 32-byte key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(filepath: str, password: str):
    """Encrypt a file using AES-256-GCM."""
    with open(filepath, 'rb') as f:
        plaintext = f.read()

    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)

    nonce = secrets.token_bytes(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Write salt + nonce + tag + ciphertext to output
    encrypted_data = salt + nonce + encryptor.tag + ciphertext
    output_path = filepath + ".enc"

    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"[+] File encrypted and saved to: {output_path}")

def decrypt_file(filepath: str, password: str):
    """Decrypt a file encrypted with AES-256-GCM."""
    with open(filepath, 'rb') as f:
        data = f.read()

    salt = data[:16]
    nonce = data[16:28]
    tag = data[28:44]
    ciphertext = data[44:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    
    try:
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    except InvalidTag:
        print("[!] Decryption failed: Incorrect password or corrupted file.")
        return

    output_path = filepath.replace(".enc", "") + ".dec"
    with open(output_path, 'wb') as f:
        f.write(plaintext)

    print(f"[+] File decrypted and saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="AES-256 File Encryptor/Decryptor")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", help="Path to file to encrypt")
    group.add_argument("-d", "--decrypt", help="Path to file to decrypt")

    parser.add_argument("-p", "--password", help="Password for encryption/decryption", required=True)

    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.encrypt, args.password)
    elif args.decrypt:
        decrypt_file(args.decrypt, args.password)

if __name__ == "__main__":
    main()

