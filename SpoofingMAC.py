import random
import os
import subprocess


def getRand():
    return random.choice("abcdef0123456789")


def newMAC():
    new = ""
    for i in range(0, 5):
        new += getRand() + getRand() + ":"
    new += getRand() + getRand()
    return new


print(os.system("ifconfig et0 | grep ether | grep -oE [0-9abcdef:]{17}"))

subprocess.call(["sudo", "ipconfig", "eth0", "down"])

new_m = newMAC()
subprocess.call(["sudo", "ipconfig", "eth0", "hw", "ether", "%s" % new_m])
subprocess.call(["sudo", "ipconfig", "eth0", "up"])

print(os.system("ifconfig et0 | grep ether | grep -oE [0-9abcdef:]{17}"))