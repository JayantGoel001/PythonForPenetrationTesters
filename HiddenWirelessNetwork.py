from scapy.all import *
from scapy.layers.dot11 import Dot11ProbeReq, Dot11ProbeResp, Dot11AssoReq

iface = "wlan0"


def h_packet(pack):
    if pack.haslayer(Dot11ProbeReq) or pack.haslayer(Dot11ProbeResp) or pack.haslayer(Dot11AssoReq):
        print("SSID identified " + pack.info)


os.system("ipconfig " + iface + "mode monitor")
print("Sniffing traffic on interface " + iface)
sniff(iface, h_packet)
