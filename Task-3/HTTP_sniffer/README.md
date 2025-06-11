## 🔍 HTTP Sniffer Tool


This is a lightweight Python-based packet sniffer that captures HTTP traffic over a specified network interface and extracts:
* Requested URLs  
* Potential login credentials transmitted over HTTP.

It is designed for educational and ethical hacking purposes to demonstrate the risks of transmitting sensitive information over unencrypted protocols like HTTP.

## 📦 Features

 - Captures HTTP requests in real time  
 - Extracts and displays requested URLs  
 - Detects potential credentials (username/password/email) in HTTP payloads  
 - Works directly with the scapy and http layers

## 🚀 How It Works

 - Listens on the specified network interface  
 - Filters packets containing HTTP request data  
 - Extracts URL paths and login-related fields from the raw data  

## 🧪 Example Output

```
[+] HTTP Request >> /login.php192.168.1.1

[+]Possible username/Password >> b'username=admin&password=123456'
```

## 🛠️ Requirements

 - Python 3.x  
 - Scapy

## 🖥️ Usage

```bash
sudo python3 http_sniffer.py
```
By default, the script uses wlan0. You may change it in the code or pass it as an argument (customization optional).

## 🛑 Legal Disclaimer
This tool is intended for educational and authorized penetration testing purposes only.
Unauthorized use of this tool to sniff traffic on networks you do not own or have explicit permission to test is illegal.


## 💡 Ideas for Extension  

 - Add HTTPS support using mitmproxy (for educational labs)  
 - Log results to a file (CSV or TXT)  
 - Detect form-based login attempts more accurately  
 - Add argument parsing with argparse