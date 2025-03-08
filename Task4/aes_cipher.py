from Crypto.Cipher import AES
import base64
import os

class AESCipher:
    def __init__(self, key):
        self.key = key.ljust(32)[:32].encode() 

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)

        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_text):
        raw = base64.b64decode(encrypted_text)
        nonce, ciphertext = raw[:16], raw[16:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')
