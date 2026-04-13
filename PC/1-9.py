import os
import platform
import uuid
import getpass
import socket

def get_mac():
    return hex(uuid.getnode())

def get_user():
    return getpass.getuser()

def get_os():
    return platform.platform()

def get_host():
    return socket.gethostname()

def get_cpu():
    return os.popen("wmic cpu get MaxClockSpeed").read()

def get_disk():
    return os.popen("wmic logicaldisk get VolumeSerialNumber").read()

def get_bios():
    return os.popen("wmic bios get SerialNumber").read()

def get_registry():
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
        value, _ = winreg.QueryValueEx(key, "MachineGuid")
        return value
    except:
        return "Нет доступа"

print("1. MAC:", get_mac())
print("2. Пользователь:", get_user())
print("3. ОС:", get_os())
print("4. Имя ПК:", get_host())
print("5. CPU (частота):", get_cpu())
print("6. Диск:", get_disk())
print("7. BIOS:", get_bios())
print("8. Реестр (MachineGuid):", get_registry())
