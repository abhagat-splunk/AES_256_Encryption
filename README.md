# AES_256_Encryption
AES 256 bit Encryption with Counter Mode.

All 3 Python files use `AES.MODE_CTR`.

`decrypt.py` uses IV and a 16 bytes key (no padding).\
`decrypt_two.py` uses IV and a key. If the key is not 32 bytes, it's padded with a constant string to make it 32 bytes.\
`decrypt_three.py` uses a random 32 bytes key. It doesn't use IV explicitly.

Pre-requisites: Please install the `pycryptodome` library before running the files. 
> https://pypi.org/project/pycryptodome/

Please run the files using the following command :`python3 <filename>.py`.
