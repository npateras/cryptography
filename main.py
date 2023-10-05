
import random
from Cryptodome.PublicKey import RSA
import rsa_generator
import replace_chars



with open("private.pem", "r") as privatePemFile:
    data_priv = privatePemFile.readlines()

print(data_priv)

data_priv2 = []
for i in data_priv:
    if i != "-----BEGIN RSA PRIVATE KEY-----\n" and i != "-----END RSA PRIVATE KEY-----":
        i = i.replace('\n','')
        data_priv2.append(i) # xoris ta first kai last alla kai xoris to new_line


# sents the list to chouse an item and it's possision in the list
sellectet_line , no_of_sellectet_line = replace_chars.method_rundom_sellect(data_priv2)

# sents the prevew sellectet item to replace 2 characters next to eachother and returns it
list_of_sellectet_line = replace_chars.change(sellectet_line)

# updates the list with the new item
data_priv2[no_of_sellectet_line] = list_of_sellectet_line

f = open("private.pem", "w")
f.write("-----BEGIN RSA PRIVATE KEY-----\n")
for i in data_priv2:
    f.write(i)
    f.write("\n")
f.write("-----END RSA PRIVATE KEY-----")
f.close()
