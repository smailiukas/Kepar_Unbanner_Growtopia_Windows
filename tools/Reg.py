import winreg

def enum_keys(key):
    keys = []
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            keys.append(subkey)
            i += 1
        except WindowsError as e:
            break
    numeric_strings = [s for s in keys if s.isnumeric()]
    return numeric_strings[0]

def get_both_keys():
    lista = []
    root_key = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKey(root_key, "")
    lista.append(enum_keys(key))
    root_key = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKey(root_key, r"SOFTWARE\Microsoft")
    lista.append(enum_keys(key))
    return lista

def delete_key(key, sub_key):
    try:
        winreg.DeleteKey(key, sub_key)
        print(f"Key {sub_key} deleted successfully.")
    except WindowsError as e:
        print(f"Error deleting key {sub_key} : {e}")

def delete_keys():
    keyster = get_both_keys()
    root_key = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKey(root_key, "", 0, winreg.KEY_ALL_ACCESS)
    sub_key = keyster[0]
    delete_key(key, sub_key)
    key_path = r"SOFTWARE\Microsoft"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
    sub_key = keyster[1]
    delete_key(key, sub_key)