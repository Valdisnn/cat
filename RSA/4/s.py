import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
s = socket.socket()
s.bind(('localhost', 9999)); s.listen(1)
c, _ = s.accept()

c.send(k.publickey().export_key()) # Шлем ключ
enc = c.recv(1024)                 # Ждем шифр

dec = PKCS1_v1_5.new(k).decrypt(enc, 0)
print(f"Получено: {dec}") # Видим результат
open('rec.bin', 'wb').write(dec)
