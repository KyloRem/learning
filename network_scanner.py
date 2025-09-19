# Network Scanner - First project 
print("Starting network scanner...")


# Ask user for an IP address
ip_input = input("Enter IP address(es) to scan (separate multiple IPs with commas): ")
print(f"You want to scan: {ip_input}")
ip_list = ip_input.split(",")


# Import the library needed for ping
import subprocess # Get the toolbox

# OLD - keeping for reference on pinging a single IP
# Try to ping the IP address
# print(f"Pinging {ip_address}...")
# result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True) # Use the tool to run ping
#
# if result.returncode == 0:
#    print(f"✅ {ip_address} is reachable!")
# else:
#    print(f"❌ {ip_address} is not reachable")


# NEW - loop through multiple IPs and scan them
for ip in ip_list:
    ip = ip.strip() # Remove any extra spaces
    print(f"Pinging {ip}...")
    result = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {ip} is reachable!")
    else:
        print(f"❌ {ip} is not reachable")
    print() # Add a blank line between results