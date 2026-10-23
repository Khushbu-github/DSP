'''
Experiment 9 — Hash Functions & Obfuscation
Question
Implement MD5 and SHA-256 hashing and demonstrate simple code obfuscation.
'''

import hashlib
import base64

text = input("Enter text: ").encode()

print("MD5:", hashlib.md5(text).hexdigest())
print("SHA256:", hashlib.sha256(text).hexdigest())

# Obfuscation
message = "Hello"
encoded = base64.b64encode(message.encode())

print("Obfuscated:", encoded)

decoded = base64.b64decode(encoded).decode()
print("Decoded:", decoded)