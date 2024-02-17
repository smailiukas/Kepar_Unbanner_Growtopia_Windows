from tools.Mac import *
from tools.Reg import *
from tools.uuid import *
from tools.unicorn import *
import time
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        try:
            change_all_mac_addresses()
        except:
            ctypes.windll.user32.MessageBoxW(None, "ERROR OCCURED:\nCould not change start the mac address refresher", "Script error", 0x40 | 0x1)
            exit()
        try:
            change_uuid_fresh()
        except:
            ctypes.windll.user32.MessageBoxW(None, "ERROR OCCURED:\nCould not change start the UUID refresher", "Script error", 0x40 | 0x1)
            exit()
        try:
            delete_keys()    
        except:
            ctypes.windll.user32.MessageBoxW(None, "ERROR OCCURED:\nCould not change start the REG-Cleaner", "Script error", 0x40 | 0x1)
            exit()            
        ctypes.windll.user32.MessageBoxW(None, ":) Kepar is always there for you", "Love You", 0x40 | 0x1)
        print_unicorn()
        time.sleep(10)

    else:
        ctypes.windll.user32.MessageBoxW(None, "Please Restart this script 'As Administrator'", "Permissions error", 0x40 | 0x1)