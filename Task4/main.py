import os
from aes_cipher import AESCipher

def encrypt_file(filename, password):
    if not os.path.exists(filename):
        print("[!] File not found!")
        return
    
    with open(filename, "rb") as f:
        plaintext = f.read()

    cipher = AESCipher(password)
    encrypted_data = cipher.encrypt(plaintext)

    with open(filename + ".enc", "w") as f:
        f.write(encrypted_data)

    print(f"[+] Encrypted file saved as {filename}.enc")

def decrypt_file(filename, password):
    if not os.path.exists(filename):
        print("[!] File not found!")
        return

    with open(filename, "r") as f:
        encrypted_data = f.read()

    cipher = AESCipher(password)
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except Exception as e:
        print("[!] Decryption failed! Wrong password?")
        return

    decrypted_filename = filename.replace(".enc", ".dec")
    with open(decrypted_filename, "wb") as f:
        f.write(decrypted_data.encode('utf-8'))


    print(f"[+] Decrypted file saved as {decrypted_filename}")

def main():
    print("=== AES-256 File Encryption Tool ===")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        filename = input("Enter file path to encrypt: ")
        password = input("Enter a password: ")
        encrypt_file(filename, password)
    elif choice == "2":
        filename = input("Enter encrypted file path to decrypt: ")
        password = input("Enter password: ")
        decrypt_file(filename, password)
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
