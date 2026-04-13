# 7. Разработать консольное приложение для генерации ключей.
from Crypto.PublicKey import RSA

k = RSA.generate(2048)
open('priv.pem', 'wb').write(k.export_key())
open('pub.pem', 'wb').write(k.publickey().export_key())
