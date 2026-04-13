# 6. Разработать визуальное приложение для шифрования/дешифрования чисел.
import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

def do(m):
    v = ent.get()
    if m == 'e': res = pub.encrypt(v.encode())
    else: res = priv.decrypt(eval(v), 0).decode()
    ent.delete(0, 'end'); ent.insert(0, res)

root = tk.Tk()
ent = tk.Entry(); ent.pack()
tk.Button(text="Enc", command=lambda: do('e')).pack()
tk.Button(text="Dec", command=lambda: do('d')).pack()
root.mainloop()
