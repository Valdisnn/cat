import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

s = socket.socket()
s.connect(('localhost', 9999))
pub = RSA.import_key(s.recv(2048)) # Берем ключ

data = open('send.bin', 'rb').read()[:200]
s.send(PKCS1_v1_5.new(pub).encrypt(data)) # Шлем шифр
