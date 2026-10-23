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