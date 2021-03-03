
import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
def int_of_string(s):
    return int(binascii.hexlify(s), 16)
def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(plaintext)
def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])

key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
data = b'this is a test message'
em = encrypt_message(key, data)
print (em)
dm = decrypt_message(key, em)
print(dm)
