# 🌐 Python IP Address Checker

A command-line tool that analyzes any IPv4 or IPv6 address and returns detailed network information — class, subnet mask, network address, broadcast address, and usable host range. Built with pure Python, no external libraries needed.

---

## Features

- **IP validation** — instantly checks if the entered IP is valid
- **Type detection** — identifies Public, Private, or Loopback addresses
- **Class detection** — determines Class A, B, or C for IPv4
- **Subnet info** — shows default subnet mask, network address, and broadcast address
- **Host range** — calculates the usable host range and total hosts
- **IPv6 support** — displays expanded and compressed forms for IPv6 addresses
- **No external libraries** — pure Python standard library only

---

## Requirements

- Python 3.6+
- No pip installs needed

---

## Usage

```bash
python ip_checker.py
```

Then enter any IP address when prompted:

```
Enter IP address: 192.168.1.50
```

---

## Example Output

### Private IPv4 (Class C)
```
Enter IP address: 192.168.1.50

Valid IP: Yes
Type: Private
Class: C
Default Subnet Mask: 255.255.255.0
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Total Hosts: 254
Usable Host Range: 192.168.1.1 - 192.168.1.254
```

### Public IPv4 (Class A)
```
Enter IP address: 8.8.8.8

Valid IP: Yes
Type: Public
Class: A
Default Subnet Mask: 255.0.0.0
Network Address: 8.0.0.0
Broadcast Address: 8.255.255.255
Total Hosts: 16777214
Usable Host Range: 8.0.0.1 - 8.255.255.254
```

### Loopback
```
Enter IP address: 127.0.0.1

Valid IP: Yes
Type: Loopback (localhost)
Class: A
Default Subnet Mask: 255.0.0.0
Network Address: 127.0.0.0
Broadcast Address: 127.255.255.255
Total Hosts: 16777214
Usable Host Range: 127.0.0.1 - 127.255.255.254
```

### IPv6
```
Enter IP address: 2001:db8::1

Valid IP: Yes
Type: Public
IP Version: IPv6
Expanded:   2001:0db8:0000:0000:0000:0000:0000:0001
Compressed: 2001:db8::1
```

### Invalid IP
```
Enter IP address: 999.999.999.999

Invalid IP address
```

---

## IP Classes Explained

| Class | Range | Default Mask | Total Hosts |
|-------|-------|--------------|-------------|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 | 16,777,214 |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 | 65,534 |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 | 254 |

---

## IP Types Explained

| Type | Description | Example |
|------|-------------|---------|
| Private | Used inside local networks, not routable on the internet | `192.168.x.x`, `10.x.x.x` |
| Public | Routable on the internet | `8.8.8.8` |
| Loopback | Points back to your own machine (localhost) | `127.0.0.1` |

---

## How It Works

1. **Validation** — uses Python's `ipaddress` module to verify the IP
2. **Type check** — checks if the IP is loopback, private, or public
3. **Class detection** — reads the first octet to determine the IP class
4. **Subnet calculation** — computes network address, broadcast, and host range using the default CIDR
5. **IPv6 handling** — detects IPv6 and displays both expanded and compressed forms

---

## Disclaimer

This tool is intended for **educational purposes** to understand IP addressing and network fundamentals.

---

## License

MIT License — free to use and modify.
