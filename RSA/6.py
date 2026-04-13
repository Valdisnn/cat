# 6. RSA числа (GUI - Исправлено)
import tkinter as tk, os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

if os.path.exists('k.pem'):
    k = RSA.import_key(open('k.pem', 'rb').read())
else:
    k = RSA.generate(2048);
    open('k.pem', 'wb').write(k.export_key())

pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)


def do(m):
    v = ent.get()
    if m == 'e':
        res = pub.encrypt(v.encode()).hex()
    else:
        res = priv.decrypt(bytes.fromhex(v), b"err").decode()

    ent.delete(0, 'end')
    ent.insert(0, res)

root = tk.Tk()
ent = tk.Entry();
ent.pack()
tk.Button(text="Enc", command=lambda: do('e')).pack()
tk.Button(text="Dec", command=lambda: do('d')).pack()
root.mainloop()
