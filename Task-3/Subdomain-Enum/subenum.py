import requests
import argparse
import concurrent.futures
import os

DEFAULT_WORDLIST = "/home/kali/raft-medium-directories-lowercase.txt"
found_subdomains = []

def request(subdomain):
    try:
        url = f"http://{subdomain}"
        response = requests.get(url, timeout=2)
        if response.status_code:
            print(f"[+] Discovered Subdomain: {subdomain}")
            found_subdomains.append(subdomain)
    except requests.exceptions.RequestException:
        pass

def load_wordlist(path):
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {path}")
        return []

def get_args():
    parser = argparse.ArgumentParser(description="Fast Subdomain Enumerator")
    parser.add_argument("-u", "--url", dest="target_url", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help=f"Path to custom wordlist (default: {DEFAULT_WORDLIST})")
    return parser.parse_args()

def main():
    args = get_args()
    target_url = args.target_url
    wordlist_path = args.wordlist if args.wordlist else DEFAULT_WORDLIST

    print(f"[*] Using wordlist: {wordlist_path}")
    words = load_wordlist(wordlist_path)
    if not words:
        print("[-] Wordlist is empty or invalid. Exiting.")
        return

    print(f"[*] Starting scan on: {target_url}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        subdomains = [f"{word}.{target_url}" for word in words]
        executor.map(request, subdomains)

    print("\n[+] Scan complete. Found subdomains:")
    for sub in found_subdomains:
        print("   -", sub)

if __name__ == "__main__":
    main()

