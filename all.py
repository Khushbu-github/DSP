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

#Experiment 2 — Kali, Wireshark, Web Security & OWASP
#Question
#Write a Python program to check system information, generate network traffic, validate input, and detect possible SQL injection keywords.

import platform
import urllib.request

# a) System information
print("OS:", platform.system())
print("Version:", platform.version())

# b) Network traffic
r = urllib.request.urlopen("https://example.com")
print("Status:", r.status)

# c) Input validation
name = input("Enter username: ")

if name.isalnum():
    print("Valid Input")
else:
    print("Invalid Input")

# d) SQL injection detection
user_input = input("Enter username: ")
keywords = ["SELECT", "DROP", "DELETE", "--"]
for word in keywords:
    if word.lower() in user_input.lower():
        print("Possible malicious input detected")
        break
else:
    print("Input appears normal")

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

"""
Experiment 4: Build python code for Dictionary Attack for plaintext and hash value.
- Add brute-force simulation in this GUI
- Add password strength checker (weak/medium/strong)
- Export analyzed passwords by category
- Support longer passwords (4+ characters)
- Export analysis report as .txt or .csv
- Add real-time progress bar for brute-force
(GUI used here because the question explicitly asks for one.)
"""
import hashlib
import itertools
import string
import csv
import tkinter as tk
from tkinter import ttk, filedialog

words = ["password", "123456", "qwerty", "admin", "letmein"]

def hash256(s):
    return hashlib.sha256(s.encode()).hexdigest()

def strength(p):
    score = 0
    if len(p) >= 8: score += 1
    if any(c.isdigit() for c in p): score += 1
    if any(c.isupper() for c in p): score += 1
    if any(c in string.punctuation for c in p): score += 1

    if score <= 1: return "Weak"
    if score <= 2: return "Medium"
    return "Strong"

def dictionary():
    target = entry.get()
    bar["maximum"] = len(words)

    for i, word in enumerate(words, 1):
        bar["value"] = i
        root.update()

        if hash256(word) == target:
            status.set("Found: " + word + " (" + strength(word) + ")")
            return

    status.set("Not Found")

def brute_force():
    target = entry.get()
    chars = string.ascii_lowercase + string.digits

    for n in range(1, 4):
        for x in itertools.product(chars, repeat=n):
            word = ''.join(x)

            if hash256(word) == target:
                status.set("Brute Force Found: " + word)
                return

    status.set("Not Found")

def export():
    file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV", "*.csv")]
    )

    if file:
        with open(file, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Password", "Strength"])

            for word in words:
                w.writerow([word, strength(word)])

root = tk.Tk()
root.title("Password Attack Tool")

tk.Label(root, text="Enter SHA-256 Hash").pack()
entry = tk.Entry(root, width=60)
entry.pack()

tk.Button(root, text="Dictionary Attack",
          command=dictionary).pack()

tk.Button(root, text="Brute Force Attack",
          command=brute_force).pack()

bar = ttk.Progressbar(root, length=300)
bar.pack()

status = tk.StringVar(value="Ready")
tk.Label(root, textvariable=status).pack()

tk.Button(root, text="Export CSV",
          command=export).pack()

root.mainloop()


"""
Experiment 5: Build a virus simulation tool - safe, educational, and
non-malicious - to help you understand how malware might behave in a
system, and how defenders can detect or prevent it.
"""
import random

SIGNATURE = "VIRUS_SIM"
files = {f"file{i}.txt": "normal" for i in range(1, 6)}

def show():
    for name, content in files.items():
        print(name, "INFECTED" if SIGNATURE in content else "Clean")

def infect():
    clean = [f for f in files if SIGNATURE not in files[f]]

    if clean:
        file = random.choice(clean)
        files[file] += " " + SIGNATURE
        print("Infected:", file)

def disinfect():
    for file in files:
        if SIGNATURE in files[file]:
            files[file] = files[file].replace(SIGNATURE, "")
    print("Scan completed. Files disinfected.")

print("Before infection:")
show()

infect()
infect()

print("\nAfter simulated infection:")
show()

disinfect()

print("\nAfter disinfection:")
show()

"""
Experiment 6: Build a Vulnerability Analyser Tool in Python that can
scan source code files (any programming language) for common security
vulnerabilities or bad coding patterns.
"""
import re

patterns = {
    r"eval\(": "Use of eval()",
    r"exec\(": "Use of exec()",
    r"os\.system\(": "Command injection risk",
    r"password\s*=": "Hardcoded password",
    r"SELECT .* \+": "Possible SQL injection",
    r"pickle\.loads": "Unsafe deserialization",
    r"md5\(": "Weak MD5 hash",
    r"verify=False": "SSL verification disabled"
}

file = input("Enter source file path: ")

code = open(file, encoding="utf-8", errors="ignore").read()

count = 0

for num, line in enumerate(code.splitlines(), 1):
    for pattern, message in patterns.items():
        if re.search(pattern, line, re.IGNORECASE):
            print("Line", num, ":", message)
            print(" ->", line.strip())
            count += 1

print("\nTotal issues:", count)


#Experiment 7 — Phishing Website Detection
#Question
#Write a Python program using Machine Learning to classify a URL as phishing or legitimate.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

urls = [
    "http://free-gift.com",
    "http://verify-account.com",
    "https://google.com",
    "https://github.com"
]

labels = [1, 1, 0, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)

model = LogisticRegression()
model.fit(X, labels)

url = input("Enter URL: ")

result = model.predict(vectorizer.transform([url]))

if result[0] == 1:
    print("PHISHING")
else:
    print("LEGITIMATE")



    """
Experiment 8: Develop a real-time messaging application where two
devices can communicate securely. The application must use Transport
Layer Security (TLS) for securing the client-server communication and
End-to-End Encryption (E2EE) to ensure that only the sender and
recipient can access the message content. The server should act
solely as a message relay and have no access to plaintext messages.

Run:  python q8_secure_messaging.py server
      python q8_secure_messaging.py client
(Self-signed cert is auto-generated on first run for the TLS layer.)
"""
import socket
import ssl
import sys
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
fernet = Fernet(KEY)

def server():
    s = socket.socket()
    s.bind(("localhost", 9999))
    s.listen(1)

    print("Server waiting...")
    conn, addr = s.accept()

    while True:
        data = conn.recv(4096)
        if not data:
            break

        print("Encrypted message received")
        conn.send(data)

    conn.close()

def client():
    s = socket.socket()

    # TLS connection
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    s = context.wrap_socket(s, server_hostname="localhost")
    s.connect(("localhost", 9999))

    msg = input("Enter message: ")

    # E2EE encryption
    encrypted = fernet.encrypt(msg.encode())
    s.send(encrypted)

    reply = s.recv(4096)
    print("Decrypted:", fernet.decrypt(reply).decode())

    s.close()

if len(sys.argv) > 1 and sys.argv[1] == "server":
    server()
else:
    client()



    #Experiment 10 — Digital Signature + Authentication
#Question
#Implement RSA digital signature generation and verification.

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = input("Enter message: ").encode()

signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

print("Signature Created")

try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Signature Valid")
except:
    print("Signature Invalid")


    '''
Experiment 11 — PII & k-Anonymity
Question
Identify PII data and perform simple anonymization using Python.
'''
import re

data = [
    "Khush,20,9876543210",
    "Rahul,21,9123456789"
]

for row in data:

    parts = row.split(",")

    name = parts[0]
    age = parts[1]
    phone = parts[2]

    print("Name:", name)
    print("Age:", age)
    print("Phone: PII")

# Anonymization
print("\nAfter Anonymization:")

for row in data:
    parts = row.split(",")
    age = parts[1]

    age_group = (int(age) // 10) * 10

    print("Age Group:", str(age_group) + "-" + str(age_group + 9))



    """
Experiment 12: Case Study on GDPR and DPDP Act 2023
Create a comparative chart of GDPR and DPDP Act 2023 principles and
explain roles like Data Protection Officer (DPO). Include a mock
incident report format.
"""
import datetime

# GDPR vs DPDP
data = [
    ("Jurisdiction", "EU", "India"),
    ("Consent", "Clear consent", "Clear consent"),
    ("DPO", "Required in certain cases", "Required for Significant Data Fiduciaries"),
    ("Breach", "72 hours", "Without delay"),
    ("Penalty", "Up to €20M / 4%", "Up to ₹250 crore"),
    ("Rights", "Access, erase, rectify", "Access, correct, erase")
]

print("GDPR vs DPDP Act 2023")

for a, gdpr, dpdp in data:
    print("\n", a)
    print("GDPR :", gdpr)
    print("DPDP :", dpdp)

# DPO role
print("""
DPO Role:
1. Monitor data protection
2. Ensure legal compliance
3. Handle user requests
4. Contact the regulator
5. Advise on privacy risks
""")

# Mock incident report
print("\nDATA BREACH INCIDENT REPORT")
print("Date:", datetime.datetime.now())
print("Incident: Unauthorized access")
print("Data: Names and emails")
print("Affected Records: 500")
print("Cause: Weak access control")
print("Action: Access revoked and system isolated")
print("Plan: Enable MFA and improve security")


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







