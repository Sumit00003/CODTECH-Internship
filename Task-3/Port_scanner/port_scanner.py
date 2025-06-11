import socket
import argparse

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\n[-] Scan aborted by user.")
            break
        except socket.gaierror:
            print("[-] Hostname could not be resolved.")
            break
        except socket.error:
            print("[-] Could not connect to server.")
            break
    return open_ports

def print_result(ip, ports):
    print(f"\nScan results for {ip}")
    print("Open Ports:\n- - - - - - -")
    for port in ports:
        print(f"Port {port} is open")

def get_args():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("-t", "--target", dest="target", help="Target IP address to scan")
    parser.add_argument("-p", "--ports", dest="ports", help="Port range to scan (e.g., 20-80)")
    options = parser.parse_args()
    if not options.target or not options.ports:
        parser.error("[-] Please specify both a target IP (-t) and a port range (-p). Use --help for more info.")
    return options

def parse_ports(port_range):
    start, end = map(int, port_range.split("-"))
    return range(start, end + 1)

options = get_args()
target_ip = options.target
port_range = parse_ports(options.ports)
open_ports = scan_ports(target_ip, port_range)
print_result(target_ip, open_ports)

