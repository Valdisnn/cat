import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

s = socket.socket(); s.connect(('localhost', 8888))
pub = RSA.import_key(s.recv(2048))

m = input("Msg: ").encode()
s.send(PKCS1_v1_5.new(pub).encrypt(m))
