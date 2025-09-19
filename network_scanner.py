# Network Scanner - First project 
print("Starting network scanner...")


# Ask user for an IP address
ip_address = input("Enter an IP address to scan: ")
print(f"You want to scan: {ip_address}")


# Import the library needed for ping
import subprocess # Get the toolbox

# Try to ping the IP address
print(f"Pinging {ip_address}...")
result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True) # Use the tool to run ping

if result.returncode == 0:
    print(f"✅ {ip_address} is reachable!")
else:
    print(f"❌ {ip_address} is not reachable")