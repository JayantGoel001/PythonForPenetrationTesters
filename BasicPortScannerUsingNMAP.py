import nmap
import sys

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]
scan_v = nmap.PortScanner()

print("\nScanning", target, "for ports 21,22,80,443 and 8080 ...\n")
portScan={}
for port in ports:
    portScan = scan_v.scan(target, str(port))
    print("Port", port, " is ", portScan['scan'][target]['tcp'][port]['state'])
print("\nHost", target, " is ", portScan['scan'][target]['status']['state'])
# py -3 BasicPortScannerUsingNMAP.py
