## 🔎 Port Scanner Tool (TCP SYN Scanner)

A simple, fast, and extensible port scanner written in Python. It allows you to check open TCP ports on a target machine. This tool is designed for use in ethical hacking labs, pentesting education, and network diagnostics.

## 📦 Features

 - Scan single hosts or IP ranges  
 - Identifies open TCP ports  
 - User-specified port range  
 - Uses socket module for standard TCP connections  
 - Supports command-line arguments for automation  

## 🧪 Sample Output

[o/p](<Task-3/Port_scanner/images>)

🛠️ Requirements 

 - Python 3.x

## 🔧 Installation

1. Clone the Repository 

```bash
git clone https://github.com/yourusername/port-scanner.git
```  
```
cd port-scanner
```  
2. Install (no external packages required)

```bash
python3 port_scanner.py --help
```

## 🖥️ Usage

```bash
python3 port_scanner.py -u 192.168.1.10
```  

## 🔍 How It Works

 - Uses Python's socket module to initiate a TCP connection.  
 - If a connection is successful, the port is considered open.  
 - Uses threading to speed up scanning across ports.

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized penetration testing only.
Scanning systems without permission is illegal and against ethical hacking principles.

## 💡 Ideas for Extension

 - Add service detection (e.g., via banners)  
 - Include UDP port scanning  
 - Export results to CSV or JSON  
 - Add scan modes: SYN scan, Stealth scan (requires raw sockets & root)
