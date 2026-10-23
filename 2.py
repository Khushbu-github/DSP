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