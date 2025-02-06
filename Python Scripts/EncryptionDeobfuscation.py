#This code is specifically for AES-256-CBC encryption. Amendments will need to be made for other encryption frameworks.

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys

#Key and IV need to be replaced
aes_key = b"examplekey0000000000000000000000" # 32 bytes with AES-256-CBC
aes_iv = b"1234567890123456"  # 16 bytes with AES-256-CBC

if len(sys.argv) != 2:
    print("Usage: python3 EncryptionDeobfuscation.py <file>")
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    ciphertext = b64decode(f.read())

cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(plaintext.decode())
