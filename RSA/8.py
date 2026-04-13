import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

if os.path.exists('k.pem'):
    k = RSA.import_key(open('k.pem', 'rb').read())
else:
    k = RSA.generate(2048)
    open('k.pem', 'wb').write(k.export_key())

pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

m = input("e/d: ")

if m == 'e':
    t = input("Текст: ").encode()
    res = b"".join(pub.encrypt(t[i:i+200]) for i in range(0, len(t), 200))
    print("Hex:", res.hex())
else:
    c = bytes.fromhex(input("Hex: "))
    res = b"".join(priv.decrypt(c[i:i+256], b"err") for i in range(0, len(c), 256))
    print("Результат:", res.decode())
