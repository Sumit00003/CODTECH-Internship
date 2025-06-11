import os
import hashlib
import json
import time

HASH_DB_FILE = "file_hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None

def scan_directory(directory):
    hash_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = calculate_hash(full_path)
            if file_hash:
                hash_data[full_path] = file_hash
    return hash_data

def load_hashes():
    if os.path.exists(HASH_DB_FILE):
        with open(HASH_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hash_data):
    with open(HASH_DB_FILE, "w") as f:
        json.dump(hash_data, f, indent=4)

def compare_hashes(old_hashes, new_hashes):
    old_files = set(old_hashes.keys())
    new_files = set(new_hashes.keys())

    added = new_files - old_files
    removed = old_files - new_files
    modified = {f for f in old_files & new_files if old_hashes[f] != new_hashes[f]}

    return added, removed, modified

def monitor(directory):
    print(f"\n[+] Scanning directory: {directory}")
    old_hashes = load_hashes()
    new_hashes = scan_directory(directory)
    added, removed, modified = compare_hashes(old_hashes, new_hashes)

    if added or removed or modified:
        print("\n[!] Changes detected:")
        if added:
            print("\n[+] Added files:")
            for f in added:
                print("   -", f)
        if removed:
            print("\n[-] Removed files:")
            for f in removed:
                print("   -", f)
        if modified:
            print("\n[*] Modified files:")
            for f in modified:
                print("   -", f)
    else:
        print("\n[✓] No changes detected.")

    save_hashes(new_hashes)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Monitor file changes using SHA-256 hash comparison.")
    parser.add_argument("directory", help="Path to directory to monitor")
    args = parser.parse_args()

    monitor(args.directory)

