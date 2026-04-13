# 8. Реализовать программу для шифрования / дешифрования текстов, работающую по алгоритму RSA. Программа должна уметь работать с текстом произвольной длины.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

t = input("Текст: ").encode()
m = input("e/d: ")

if m == 'e':
    res = b"".join(pub.encrypt(t[i:i+200]) for i in range(0, len(t), 200))
    print(res.hex())
else:
    c = bytes.fromhex(input("Hex: "))
    res = b"".join(priv.decrypt(c[i:i+256], 0) for i in range(0, len(c), 256))
    print(res.decode())
