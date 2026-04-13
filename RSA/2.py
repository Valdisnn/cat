# 2. Разработать визуальное приложение для шифрования/дешифрования изображений.
import tkinter as tk
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

k = RSA.generate(2048)
pub, priv = PKCS1_v1_5.new(k.publickey()), PKCS1_v1_5.new(k)

def do(m):
    p = filedialog.askopenfilename()
    d = open(p, 'rb').read()
    if m == 'e': open(p+'.enc','wb').write(pub.encrypt(d[:200]))
    else: open(p+'.dec.png','wb').write(priv.decrypt(d, 0))

root = tk.Tk()
tk.Button(text="Enc", command=lambda: do('e')).pack()
tk.Button(text="Dec", command=lambda: do('d')).pack()
root.mainloop()
