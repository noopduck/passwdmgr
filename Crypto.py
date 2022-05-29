import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Crypto():
    def __init__(self, hash):
        salt = bytes(hash, 'utf8')

        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )

        self.key = base64.urlsafe_b64encode(self.kdf.derive(b"{hash}"))

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def createKey(self, password):
        self.key = base64.urlsafe_b64encode(self.kdf.derive(b"{password}"))

    def encrypt(self, blob):
        f = Fernet(self.key)
        msg = f.encrypt(blob)
        return msg

    def decrypt(self, blob):
        f = Fernet(self.key)
        msg = f.decrypt(blob)
        return msg

