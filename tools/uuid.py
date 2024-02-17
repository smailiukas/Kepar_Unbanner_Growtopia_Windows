import uuid
import winreg

def generate_random_uuid():
    return uuid.uuid4()

def change_uuid_fresh():
    new_uuid = str(uuid.uuid4())
    key_path = r"SOFTWARE\Microsoft\Cryptography"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)

    winreg.SetValueEx(key, "MachineGuid", 0, winreg.REG_SZ, new_uuid)
    winreg.CloseKey(key)