import ipaddress

ip = input("Enter IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)
    print("Valid IP: Yes")

    if ip_obj.is_loopback:
        print("Type: Loopback (localhost)")
    elif ip_obj.is_private:
        print("Type: Private")
    else:
        print("Type: Public")

    if isinstance(ip_obj, ipaddress.IPv4Address):
        first_octet = int(ip.split(".")[0])
        if 1 <= first_octet <= 126:
            ip_class = "A"
            default_mask = "255.0.0.0"
            cidr = 8
        elif 128 <= first_octet <= 191:
            ip_class = "B"
            default_mask = "255.255.0.0"
            cidr = 16
        elif 192 <= first_octet <= 223:
            ip_class = "C"
            default_mask = "255.255.255.0"
            cidr = 24
        else:
            ip_class = "Other"
            default_mask = "N/A"
            cidr = None

        print(f"Class: {ip_class}")
        print(f"Default Subnet Mask: {default_mask}")

        if cidr:
            network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
            first_host = next(network.hosts())
            last_host = network.broadcast_address - 1
            print(f"Network Address: {network.network_address}")
            print(f"Broadcast Address: {network.broadcast_address}")
            print(f"Total Hosts: {network.num_addresses - 2}")
            print(f"Usable Host Range: {first_host} - {last_host}")

    elif isinstance(ip_obj, ipaddress.IPv6Address):
        print("IP Version: IPv6")
        print(f"Expanded: {ip_obj.exploded}")
        print(f"Compressed: {ip_obj.compressed}")

except ValueError:
    print("Invalid IP address")
