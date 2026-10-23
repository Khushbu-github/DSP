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