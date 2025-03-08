# ADVANCED-ENCRYPTION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MAHESH KUMAR P

*INTERN ID*: CT08SIK

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

# DESCRIPTION

# Task 4: File Encryption & Decryption Tool
This tool provides secure encryption and decryption of files using the AES-256 algorithm, ensuring data confidentiality. It allows users to encrypt sensitive files and later decrypt them with a password.

# Features Implemented
•AES-256 Encryption → Uses Advanced Encryption Standard (AES) for high security.

•Password-Based Key Derivation → Converts user passwords into strong cryptographic keys.

•File Integrity Protection → Prevents unauthorized modification of encrypted files.

•User-Friendly Interface → Command-line interaction for ease of use.

# Libraries Used
•pycryptodome (Crypto.Cipher.AES) → Performs AES-256 encryption/decryption.

•os → Handles file operations.

•getpass → Ensures passwords are entered securely.

•base64 → Encodes encrypted data for storage.

# How It Works
•The user selects an option: Encrypt or Decrypt.

•If encrypting:

  •The user enters a file path and password.
  
  •The tool generates a strong encryption key.
  
  •The file is encrypted and saved as <filename>.enc.
  
•If decrypting:

  •The user provides the encrypted file and password.
  
  •The tool derives the encryption key and decrypts the file.
  
  •The original file is restored if the password is correct.
  
•Errors are handled for missing files, incorrect passwords, and data corruption.

# Outcome
•Ensures data security using AES-256 encryption.

•Prevents unauthorized access to sensitive files.

•Provides a simple yet powerful encryption tool for users.

# OUTPUT

<img width="770" alt="Image" src="https://github.com/user-attachments/assets/217ea2e3-2858-4c84-92e2-92ff0ab1d04a" />

<img width="775" alt="Image" src="https://github.com/user-attachments/assets/0ac3a0ed-01a5-4d94-9bc8-74a51a9ae895" />
