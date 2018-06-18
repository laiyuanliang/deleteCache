import rsa
from Crypto.PublicKey import RSA
e = 65537
n = int('846408e74f39c28559f0bcd7c116e48911d94f415df4173921fbbd6a43a49908b4050d0550ae7f0d2b20e1914f2eeafb08beb5453b5f697c2c596a624ac4cd4156b6742abd7fcced03fee36cf0389c948ca9ecb5b242d6733fc342d8997614bf5d8cf77b188d88c6ae07ac1696b9c784b9aea35e21729fdded528994625a151e48eb239824a1a4a40369e8cebb49461562a6cfd41138513304a09fd0a20ff8f0f7ba5e6acff6d70957d8b0b92e6d10ead31a0145624f77454966c70b2b74a4884adfce159021fe6154cd1c7787dd9577febea8c8a4c44f52e83edfa7c64ecf2226cb584d468de5bfc89998125613441074e904b7d51bf74b36bf683e1334b777', 16)
print("######## this is number n #########")
print(n)
print("#################################")

key_params = (n, e)
pub_key = RSA.construct(key_params)

message = 'hahahua@123'
cryto = rsa.encrypt(message.encode(),pub_key)

print(type(cryto))
print("************** there is crypt password *******")
print(cryto.hex())

