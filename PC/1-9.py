import hashlib, os, platform, uuid

# 1. Функции сбора данных (каждая в одну строку)
def get_mac(): return str(uuid.getnode())
def get_user(): return os.getlogin()
def get_disk(): return os.popen('wmic diskdrive get serialnumber').read().strip()
def get_bios(): return os.popen('wmic bios get serialnumber').read().strip()
def get_cpu():  return os.popen('wmic cpu get maxclockspeed').read().strip()
def get_os():   return platform.version()
def get_host(): return platform.node()

# 2. Таблица вариантов
variants = {
    1: lambda: (get_disk(), get_mac()),  # Серийный номер диска, MAC-адрес
    2: lambda: ("Registry", get_cpu()),   # Информация из реестра, частота процессора
    3: lambda: (get_os(), get_mac()),    # Версия ОС, MAC-адрес
    4: lambda: (get_user(), get_disk()), # Имя пользователя, серийный номер диска
    5: lambda: (get_host(), "Registry"),  # Название компьютера, информация из реестра
    6: lambda: (get_bios(), get_user()), # Версия БИОС, имя пользователя
    7: lambda: (get_disk(), get_user()), # Серийный номер диска, имя пользователя
    8: lambda: (get_user(), get_cpu()),  # Имя пользователя, частота процессора
    9: lambda: (get_mac(), get_cpu())    # MAC-адрес, частота процессора
}

# 3. Основная логика
v = int(input("Введите номер варианта (1-9): "))
p1, p2 = variants[v]()
hwid = hashlib.sha256(f"{p1}{p2}".encode()).hexdigest()

try:
    if open('lic.dat').read() == hwid:
        print("Доступ разрешен!")
    else:
        print("Ошибка: компьютер не совпадает"); exit()
except:
    with open('lic.dat', 'w') as f: f.write(hwid)
    print("Лицензия создана. Перезапустите программу.")
