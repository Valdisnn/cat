# 1. Разработать консольное приложение для шифрования/дешифрования произвольных файлов с помощью алгоритма RSA.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

path, mode = input("Путь: "), input("e/d: ")
if mode == 'e':
    res = pub.encrypt(open(path, 'rb').read()[:200])
    open(path + '.enc', 'wb').write(res)
else:
    res = priv.decrypt(open(path, 'rb').read(), 0)
    open(path + '.dec', 'wb').write(res)
