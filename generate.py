from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pyotp import TOTP
import base64
import hashlib


# fill these with values explained in README.md
android_ssaid = b''
seed = b''

key = hashlib.sha256(android_ssaid + b'unknownnull').digest()
aes = AES.new(key, AES.MODE_CBC, b'\x00'*16)
data = unpad(aes.decrypt(base64.b64decode(seed)), 8)
data = base64.b32encode(bytes.fromhex(data.decode('utf-8')))

totp = TOTP(data, interval = 60)
print(totp.now())
