import os
import json, binascii
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter


def int_of_string(s):
    return int(binascii.hexlify(s), 16)


data = b"this is a test message"
key = get_random_bytes(32)
print(key)
cipher = AES.new(key, AES.MODE_CTR)
print (b64encode(cipher.nonce).decode('utf-8'))
ct_bytes = cipher.encrypt(data)
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
print(result)


try:
    b64 = json.loads(result)
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    pt = cipher.decrypt(ct)
    print("The message was: ", pt)
except Exception as e:
    print("Incorrect decryption: {}".format(e))