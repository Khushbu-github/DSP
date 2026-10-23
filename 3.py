#Experiment 3 — CIA Triad
#Question
#Write a Python program to demonstrate Confidentiality, Integrity and Availability.
import hashlib

# Confidentiality
message = "Secret Data"

key = "123"
encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + int(key))

print("Encrypted:", encrypted)

# Integrity
data = "Hello"
hash1 = hashlib.sha256(data.encode()).hexdigest()

data = "Hello!"
hash2 = hashlib.sha256(data.encode()).hexdigest()

if hash1 == hash2:
    print("Integrity OK")
else:
    print("Data Modified")

# Availability
server = True

if server:
    print("Server Available")
else:
    print("Server Down")

'''
What is CIA?
C — Confidentiality → only authorized people can see data.

I — Integrity → data should not be modified.

A — Availability → system should be available when needed.
Easy memory trick
CIA = Secret + Same + Service

- Secret → Confidentiality
- Same → Integrity
- Service available → Availability
'''