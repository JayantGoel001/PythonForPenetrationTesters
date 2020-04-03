import sys
import requests
import socket
import json

if len(sys.argv)<2:
    print("Usage: "+sys.argv[0]+"<url>")
    sys.exit(1)

req=requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

getHostBy=socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+getHostBy+"\n")

req_two=requests.get("https://ipinfo.io/"+getHostBy+"/json")

resp=json.loads(req_two.text)

print("Location: "+resp['loc'])
print("Region: "+resp['region'])
print("City: "+resp['city'])
print("Country: "+resp['country'])

# py -3 GrabbingBanners.py "google.com"