from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

AES_KEY = get_random_bytes(24)

def encrypt_data(data):
    cipher = AES.new(AES_KEY, AES.MODE_EAX)

    data_bytes = data.encode("utf-8")

    ciphertext, tag = cipher.encrypt_and_digest(data_bytes)

    return cipher.nonce, tag, ciphertext


def decrypt_data(nonce, tag, ciphertext):
    cipher = AES.new(AES_KEY, AES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext
