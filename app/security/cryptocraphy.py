from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


aes_key = get_random_bytes(24)

def encrypt_data(data):
    global aes_key
    cipher = AES.new(key=aes_key, mode=AES.MODE_EAX)

    ciphertext = cipher.encrypt(data)
    

    return ciphertext

def decrypt_data(data):
    global aes_key
    cipher = AES.new(key=aes_key, mode=AES.MODE_EAX)

    nonce = cipher.nonce
    
    cipher = AES.new(key=aes_key, mode=AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(data)

    return plaintext


email = b'athosferreirasn@gmail.com'
crypt = encrypt_data(email)
print(crypt)
print('---------------------------------')
decrypt = decrypt_data(email)
print(decrypt)