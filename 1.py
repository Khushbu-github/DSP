#Experiment 1 — Basic Security Tools & Cryptography
#Write a Python program to demonstrate password strength checking, authentication, IP identification, Caesar cipher, and hexadecimal encoding/decoding.
import socket

# a) Password strength
p = input("Enter password: ")
if len(p) >= 8:
    print("Strong password")
else:
    print("Weak password")

# b) Authentication
u = input("Username: ")
p = input("Password: ")

if u == "student" and p == "1234":
    print("Login Successful")
else:
    print("Invalid Login")

# c) Local IP
print("IP Address:", socket.gethostbyname(socket.gethostname()))

# d) Caesar Cipher
text = input("Enter text: ")
shift = 3

encrypted = ""
for ch in text:
    encrypted += chr(ord(ch) + shift)

print("Encrypted:", encrypted)

# e) Hex encoding/decoding
text = "Hello"
encoded = text.encode().hex()
decoded = bytes.fromhex(encoded).decode()

print("Hex:", encoded)
print("Decoded:", decoded)