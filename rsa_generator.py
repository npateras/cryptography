import random
from Cryptodome.PublicKey import RSA

key = RSA.generate(1024)
f = open("private.pem", "wb")
f.write(key.exportKey('PEM'))
f.close()

f = open("private_unchaged.pem","wb")
f.write(key.exportKey('PEM'))
f.close()

pubkey = key.publickey()
f = open("public.pem", "wb")
f.write(pubkey.exportKey('OpenSSH'))
f.close()
