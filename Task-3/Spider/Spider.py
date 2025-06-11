import re
import urllib.parse as urlparse
import requests
import argparse

visited_links = []

def extract_links_from(url):
    try:
        response = requests.get(url)
        return re.findall(r'(?:href=")(.*?)"', response.content.decode(errors="ignore"))
    except requests.RequestException as e:
        print(f"[-] Error requesting {url} - {e}")
        return []

def crawl(url, base_url):
    try:
        href_links = extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if '#' in link:
                link = link.split('#')[0]

            if link not in visited_links and base_url in link:
                visited_links.append(link)
                print("[+] Found link:", link)
                crawl(link, base_url)

    except KeyboardInterrupt:
        print("\n[+] Ctrl+C detected. Stopping crawl.")

def get_args():
    parser = argparse.ArgumentParser(description="Simple Python Web Crawler")
    parser.add_argument("-u", "--url", dest="target_url", required=True, help="Base URL to start crawling from")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print("[*] Starting crawl on:", args.target_url)
    crawl(args.target_url, args.target_url)

