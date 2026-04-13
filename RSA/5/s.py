import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
s = socket.socket(); s.bind(('localhost', 8888)); s.listen(1)
c, _ = s.accept()

c.send(k.publickey().export_key())
msg = c.recv(1024)
res = PKCS1_v1_5.new(k).decrypt(msg, 0).decode()
print(f"Сообщение: {res}") # Видим текст
