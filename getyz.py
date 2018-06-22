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
print('FFFFFFFFFFFFFFFFFFFFFFFFFFFF')
print(pub_key)
print('FFFFFFFFFFFFFFFFFFFFFFFFFFFF')
message = 'hahnhua@123'
cryto = rsa.encrypt(message.encode(),pub_key)

print(cryto)
