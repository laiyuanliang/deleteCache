import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import rsa
from Crypto.PublicKey import RSA

url0 = 'http://yzcs.geotmt.com/civp/getview/web/o/mlogin'
head0 = {'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

r = requests.get(url0, headers = head0)  # within this responce, we get JSESSIONID/identifyingCodeId/baseUniqueKey for RSAKEY

cookie_for_RsaKey = {}
#cookie_for_RsaKey['JSESSIONID'] = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
cookie_for_RsaKey['baseUniqueKey'] = r.headers['Set-Cookie'].split(',')[1].split(';')[0].split('=')[1]
cookie_for_RsaKey['identifyingCodeId']= r.headers['Set-Cookie'].split(',')[2].split(';')[0].split('=')[1]
print(cookie_for_RsaKey)

url2 = 'http://yzcs.geotmt.com/civp/getview/com/o/getwebrsapublickey'
head_for_RsaKey = {'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r_for_RsaKey = requests.get(url2, headers = head_for_RsaKey, cookies = cookie_for_RsaKey)

public_module = r_for_RsaKey.headers['Set-Cookie'].split(',')[1].split(';')[0].split('=')[1]
e = 65537
n = int(public_module, 16)
key_params = (n, e)
pub_key = RSA.construct(key_params)

message = 'hahnhua@123'
cryto = rsa.encrypt(message.encode(),pub_key)

cookie_to_login = {}
cookie_to_login['baseUniqueKey'] = r.headers['Set-Cookie'].split(',')[1].split(';')[0].split('=')[1]
cookie_to_login['identifyingCodeId'] = r.headers['Set-Cookie'].split(',')[2].split(';')[0].split('=')[1]
cookie_to_login['publicKeyModule'] = r_for_RsaKey.headers['Set-Cookie'].split(',')[1].split(';')[0].split('=')[1]
cookie_to_login['publicKeyEmpoent'] = '10001'
cookie_to_login['RSAKeySize'] = '2048'
cookie_to_login['privateKeyAttributeName'] = r_for_RsaKey.headers['Set-Cookie'].split(',')[4].split(';')[0].split('=')[1] 
#print(cookie_to_login)
url3 = 'http://yzcs.geotmt.com/civp/getview/web/o/login'
head_for_login = head_for_RsaKey

user = 'laijianhua'
pwd = cryto.hex()
r_for_login = requests.get(url3, headers = head_for_login, cookies = cookie_to_login, auth = HTTPBasicAuth('laijianhua',pwd))
print(r_for_login.content)

#coolie send to login
#Cookie: baseUniqueKey=ATB%3A119e7f7d-7dea-463e-aeaa-46d41d2b55d9km50h; identifyingCodeId=""; JSESSIONID=942FCD1483344723B6FB46848E3D8354; publicKeyModule=846408e74f39c28559f0bcd7c116e48911d94f415df4173921fbbd6a43a49908b4050d0550ae7f0d2b20e1914f2eeafb08beb5453b5f697c2c596a624ac4cd4156b6742abd7fcced03fee36cf0389c948ca9ecb5b242d6733fc342d8997614bf5d8cf77b188d88c6ae07ac1696b9c784b9aea35e21729fdded528994625a151e48eb239824a1a4a40369e8cebb49461562a6cfd41138513304a09fd0a20ff8f0f7ba5e6acff6d70957d8b0b92e6d10ead31a0145624f77454966c70b2b74a4884adfce159021fe6154cd1c7787dd9577febea8c8a4c44f52e83edfa7c64ecf2226cb584d468de5bfc89998125613441074e904b7d51bf74b36bf683e1334b777; publicKeyEmpoent=10001; RSAKeySize=2048; privateKeyAttributeName=8673f665-3e7a-41f7-a8cd-aaf3a0da946f

