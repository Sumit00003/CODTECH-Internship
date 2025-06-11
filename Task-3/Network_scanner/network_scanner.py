import scapy.all as spa
import argparse

def scan(ip):
    arp_req = spa.ARP(pdst=ip)
    broadcast = spa.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_req_bro = broadcast / arp_req
    ans = spa.srp(arp_req_bro, timeout=1, verbose=False)[0]
    client_list = []
    for i in ans:
        client_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP\t\t\tMAC ADDRESS\n- - - - - - - - - - - - - - - - - - - -")
    for i in result_list:
        print(i["ip"] + "\t\t" + i["mac"])

def get_args():
    parser = argparse.ArgumentParser(description="Network scanner using ARP requests")
    parser.add_argument("-r", "--range", dest="target", help="IP range to scan (e.g., 192.168.1.1/24)")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP range using -r or --range. Use --help for more info.")
    return options

options = get_args()
scan_result = scan(options.target)
print_result(scan_result)

