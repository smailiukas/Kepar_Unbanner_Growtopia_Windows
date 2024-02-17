import subprocess
import re
import random

import psutil

def get_interfaces():
    data = psutil.net_if_stats()
    interfaces = []
    for key, value in data.items():
        interfaces.append(key)
    return interfaces

def get_random_mac_address():
    """Generate and return a random MAC address."""
    mac = [0x02, 0x42, random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def get_current_mac_address(iface):
    # Use the ipconfig command to get the interface details, including the MAC address
    output = subprocess.check_output(f"ipconfig /all", shell=True).decode()
    matches = re.findall(r"Physical Address[.]*: (.+)", output)
    for match in matches:
        if iface.lower() in match.lower():
            return match.strip()

def change_mac_address(iface, new_mac_address):
    # Disable the network interface
    subprocess.check_output(f"netsh interface set interface {iface} admin=disable", shell=True)
    # Change the MAC
    subprocess.check_output(f"netsh interface set interface {iface} newmac={new_mac_address}", shell=True)
    # Enable the network interface again
    subprocess.check_output(f"netsh interface set interface {iface} admin=enable", shell=True)

def change_all_mac_addresses():
    # Iterate through network interfaces and change their MAC addresses
    for iface in get_interfaces():
        try:
            change_mac_address(iface, get_random_mac_address())
        except:
            pass

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python Mac Changer on Windows")
    parser.add_argument("interface", help="The network interface name on Windows")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
    args = parser.parse_args()
    
    iface = args.interface

    if args.random:
        # If random parameter is set, generate a random MAC
        new_mac_address = get_random_mac_address()
    elif args.mac:
        # If mac is set, use it instead
        new_mac_address = args.mac

    # Get the current MAC address
    old_mac_address = get_current_mac_address(iface)
    print("[*] Old MAC address:", old_mac_address)

    # Change the MAC address
    change_mac_address(iface, new_mac_address)

    # Check if it's really changed
    new_mac_address = get_current_mac_address(iface)
    print("[+] New MAC address:", new_mac_address)