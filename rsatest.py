from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

random_generator = Random.new().read
rsa = RSA.generate(1024,random_generator)

pri_key = rsa.exportKey('PEM')
pub_key = rsa.publickey().exportKey('PEM')

with open('pri_key.pem','wb+') as f:
    f.write(pri_key)

with open('pub_key.pem','wb+') as f:
    f.write(pub_key)

message = 'hello ghost, this is a plian text'
with open('pub_key.pem','rb+') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = cipher.encrypt(message.encode())
    print(cipher_text)

private_key = open('pri_key.pem','rb+').read()
pri_rsa_key = RSA.importKey(private_key)
pri_cipher = Cipher_pkcs1_v1_5.new(pri_rsa_key)
hint = 'failed during decrpt'
text = pri_cipher.decrypt(cipher_text,hint)
print(text)
