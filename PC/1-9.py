import hashlib, os, platform, uuid

# 1. Сбор данных под Windows (через popen)
def get_mac():  return str(uuid.getnode())
def get_user(): return os.getlogin()
def get_os():   return platform.version()
def get_host(): return platform.node()
def get_disk(): return os.popen('wmic diskdrive get serialnumber').read().split()[1]
def get_bios(): return os.popen('wmic bios get serialnumber').read().split()[1]
def get_cpu():  return os.popen('wmic cpu get maxclockspeed').read().split()[1]

# 2. Таблица вариантов
variants = {
    1: lambda: (get_disk(), get_mac()), # 1. Серийный номер раздела жесткого диска, MAC-адрес сетевой карты
    2: lambda: ("Registry", get_cpu()),  # 2. Информация из реестра, тактовая частота процессора
    3: lambda: (get_os(), get_mac()),   # 3. Версия операционной системы, MAC-адрес сетевой карты
    4: lambda: (get_user(), get_disk()),# 4. Имя пользователя, серийный номер раздела жесткого диска
    5: lambda: (get_host(), "Registry"), # 5. Название компьютера, информация из реестра
    6: lambda: (get_bios(), get_user()),# 6. Версия БИОС, имя пользователя
    7: lambda: (get_disk(), get_user()),# 7. Серийный номер раздела жесткого диска, имя пользователя
    8: lambda: (get_user(), get_cpu()), # 8. Имя пользователя, тактовая частота процессора
    9: lambda: (get_mac(), get_cpu()),  # 9. MAC-адрес сетевой карты, тактовая частота процессора
}

# 3. Логика лицензии
v = int(input("Вариант (1-9): "))
p1, p2 = variants[v]()
hwid = hashlib.sha256(f"{p1}{p2}".encode()).hexdigest()

if os.path.exists('lic.dat'):
    if open('lic.dat').read() == hwid:
        print("OK: Доступ разрешен")
    else:
        print("FAIL: Другой компьютер"); exit()
else:
    open('lic.dat', 'w').write(hwid)
    print("Лицензия создана. Перезапустите.")
