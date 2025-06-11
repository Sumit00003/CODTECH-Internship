# 🔍 File Change Monitor (Python)

A lightweight Python tool to monitor file changes in a directory by calculating and comparing **SHA-256 hash values**. Ideal for security enthusiasts, system admins, and anyone wanting to track unauthorized or accidental file modifications.

---

## 📦 Features

- ✅ Detects **added**, **deleted**, and **modified** files.  
- 🔐 Uses **SHA-256** hashing for file integrity checking.  
- 🧠 Stores hashes in a local JSON database.  
- 💡 CLI-based and beginner-friendly.  
- 💾 Portable: no third-party dependencies.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7 or higher  

### 📥 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/file-change-monitor.git  
cd file-change-monitor
```
## 🏃 Usage
Run the script with the path to the directory you want to monitor:  
```
bash
python file_change_monitor.py /path/to/your/directory
```  
On the first run, it will create a baseline hash snapshot (file_hashes.json). On every Execution, it will:  

 - Show newly added files  
 - Report modified files
 - Detect deleted files



## 📁 Example Output

![image](<images/Screenshot_2025-06-07_06_50_30 copy.png>)

## 🛡️ Use Cases

* Detect unauthorized file changes in sensitive directories  
* Track changes in config files or codebases  
* Monitor your own project folder integrity

## 🧠 Future Improvements

* Real-time monitoring using watchdog  
* Logging to a separate file  
* Email/SMS alerts

