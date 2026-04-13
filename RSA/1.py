# 1. Разработать консольное приложение для шифрования/дешифрования произвольных файлов с помощью алгоритма RSA.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import os

if not os.path.exists('key.pem'):
    k = RSA.generate(2048)
    open('key.pem', 'wb').write(k.export_key())
else:
    k = RSA.import_key(open('key.pem', 'rb').read())

pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

path, mode = input("Путь: "), input("e/d: ")

if mode == 'e':
    data = open(path, 'rb').read()[:200]
    open(path + '.enc', 'wb').write(pub.encrypt(data))
else:
    res = priv.decrypt(open(path, 'rb').read(), b"error")
    open(path + '.dec', 'wb').write(res)
