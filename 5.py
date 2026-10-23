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