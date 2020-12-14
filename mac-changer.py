#! /usr/bin/python3

#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   MAC changer
#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import subprocess
import optparse

#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC addr")
    parser.add_option("-m","--mac", dest="new_mac", help="new MAC addr")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] need specify interface ...")
    elif not options.new_mac:
        parser.error("[-] need specify new MAC ...")
    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address to {new_mac} on {interface}")
    print(f"ifconfig {interface} down")
    print(f"ifconfig {interface} hw ether {new_mac}")
    print(f"ifconfig {interface} down")

    #subprocess.call(["ifconfig", interface, "down"])
    #subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    #subprocess.call(["ifconfig", interface, "up"])

#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





options = get_arguments()
change_mac(options.interface, options.new_mac)






