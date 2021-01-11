#!/usr/bin/python3


##################################################
#   Socket practice
##################################################

import socket
import sys



hostname = socket.gethostname()
ip_s = socket.gethostbyname(hostname)


def family_sockadd(target):
    print("----------"*9)
    try :
        for res in socket.getaddrinfo(target, None, proto=socket.IPPROTO_TCP):
            family = res[0]
            sockaddr = res[4]
            print (f"\n[+] family: {family}\n[+] socket address: {sockaddr}")
    except socket.gaierror:
        print("[+] Invalid!")

    print("----------"*9)





print(f"[+] Server ({hostname} | {ip_s}) online ... ")

exapp = False

while exapp == False:
    print("\n")
    print("[+] Choose options ...\n\n")
    print("[1] get family and socket address info")
    print("[2] ---EXIT---")
    print("[9] **loop again**")
    use = input("I want :   ")
    if int(use) == 1:
        print("[+] Command: 1 , starting ...")
        family_sockadd("www.google.com")
        continue
    if int(use) == 2:
        exapp = True
        break

    if int(use) == 9:
        continue

print("[+] Server closing ...")




