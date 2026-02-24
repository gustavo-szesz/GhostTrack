import json
import requests
import time
import os
import phonenumbers
import socket
import ipaddress
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# ...existing code...

def is_private_ip(ip):
    """Check if IP is private/internal"""
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


def get_hostname(ip):
    """Get hostname from IP address"""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return "Unknown"


def get_mac_address(ip):
    """Get MAC address from IP (Linux/Mac only)"""
    try:
        result = os.popen(f"arp -n {ip} | grep {ip}").read()
        if result:
            return result.split()[2]
    except:
        pass
    return "Unable to retrieve"


@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")
    print()
    
    # Check if IP is private/internal
    if is_private_ip(ip):
        print(f' {Wh}============= {Gr}SHOW INFORMATION INTERNAL IP {Wh}=============')
        print(f"{Wh}\n IP target    :{Gr}", ip)
        print(f"{Wh} Type         :{Gr} Private/Internal IP")
        print(f"{Wh} Hostname     :{Gr}", get_hostname(ip))
        print(f"{Wh} MAC Address  :{Gr}", get_mac_address(ip))
        print(f"{Wh} Status       :{Gr}", "Reachable (Local Network)" if os.system(f"ping -c 1 {ip} > /dev/null 2>&1") == 0 else "Unreachable")
    else:
        # External IP handling (existing code)
        print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        time.sleep(2)
        print(f"{Wh}\n IP target       :{Gr}", ip)
        print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        # ...existing code...