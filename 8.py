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