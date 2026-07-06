import socket

# Step 1: Get local hostname
local_hostname = socket.gethostname()

# Step 2: Get list of IP addresses associated with hostname
ip_address = socket.gethostbyname_ex(local_hostname)[2]

# Step 3: Filter out loopback addresses
filtered_ips = [ip for ip in ip_address if not ip.startswith("127.")]

# Step 4: Extract and print the first IP address
if filtered_ips:
    print("Local IP Address:", filtered_ips[0])
else:
    print("No valid IP address found.")