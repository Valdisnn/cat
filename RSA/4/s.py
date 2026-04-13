# 4. Сервер файлов
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
s = socket.socket()
s.bind(('localhost', 9999)); s.listen(1)
c, _ = s.accept()
c.send(k.publickey().export_key())
enc = c.recv(1024)
open('rec.bin', 'wb').write(PKCS1_v1_5.new(k).decrypt(enc, 0))
