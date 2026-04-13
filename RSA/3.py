# 3. RSA произвольные файлы (GUI - Исправлено)
import tkinter as tk
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import os

if os.path.exists('k.pem'):
    k = RSA.import_key(open('k.pem', 'rb').read())
else:
    k = RSA.generate(2048)
    open('k.pem', 'wb').write(k.export_key())

pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

def do(m):
    p = filedialog.askopenfilename()
    if not p: return
    data = open(p, 'rb').read()

    if m == 'e':
        res = pub.encrypt(data[:200]) + data[200:]
        open(p + '.enc', 'wb').write(res)
    else:
        res = priv.decrypt(data[:256], b"error") + data[256:]
        open(p + '.dec', 'wb').write(res)
    print("Готово")

root = tk.Tk()
tk.Button(text="Enc", command=lambda: do('e')).pack()
tk.Button(text="Dec", command=lambda: do('d')).pack()
root.mainloop()
    