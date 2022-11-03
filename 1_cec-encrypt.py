from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open("data/.cec", mode="r") as cec_password:
    secret = cec_password.read()

data = secret.strip().encode()
key = get_random_bytes(16)
with open("data/cec.key", "wb") as binary_file:
    binary_file.write(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("data/cec.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
file_out.close()
