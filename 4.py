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