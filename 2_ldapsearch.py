#!/usr/bin/env python3
import subprocess
import sys
from Crypto.Cipher import AES

file_in = open("data/cec.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again
with open("data/cec.key", mode="rb") as key_file:
    key = key_file.read()
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
pwd = data.decode()

with open("data/all.csv", "r") as a_file:
  for line in a_file:
    user = line.strip()
    command = 'ldapsearch -LLL -b "OU=Employees,OU=Cisco Users, DC=cisco, DC=com" -D \'anasharm@cisco.com\' -w \'' + pwd + '\' \'(description=' + user + ')\' mail employeeType'
    ldap = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, bufsize=1, universal_newlines=True)
    for line in ldap.stdout:
        sys.stdout.write(line)
    ldap.wait()
    exit_code = ldap.returncode
    if exit_code != 0:
        raise RuntimeError(f"Shell command failed with exit code {exit_code}. Command: `{command}`")
