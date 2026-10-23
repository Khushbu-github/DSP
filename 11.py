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