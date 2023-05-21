import platform
import subprocess
import csv

# Function to check if Nmap is installed
def check_nmap_installed():
    try:
        subprocess.run(['nmap', '-v'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

# Function to run Nmap scan and save the output
def run_nmap_scan(scan_type, network_range, output_file):
    command = ['nmap']
    if scan_type == 'ping':
        command += ['-sn']
    elif scan_type == 'version':
        command += ['-sV']

    command += [network_range]

    with open(output_file + '.txt', 'w') as txt_file, open(output_file + '.csv', 'w', newline='') as csv_file:
        subprocess.run(command, stdout=txt_file, stderr=subprocess.DEVNULL)
        subprocess.run(['nmap', '-oX', '-', network_range], stdout=csv_file, stderr=subprocess.DEVNULL)

    print(f"Nmap scan completed. Output saved to '{output_file}.txt' and '{output_file}.csv'.")

# Detect the OS
current_os = platform.system()

# Check if Nmap is installed
if not check_nmap_installed():
    print("Nmap is not installed. Please install Nmap before running the code again.")
    sys.exit(1)

print("Nmap is installed.")

# Ask for the number of networks to scan
num_networks = int(input("Enter the number of networks to scan: "))

# Perform network scanning
for i in range(num_networks):
    network_range = input(f"Enter the IP range for network {i + 1}: ")

    # Ask for the scan type
    scan_type = input("Which scan do you want to perform? (ping/version): ")

    # Ask for the name of the output file
    output_file = input("Enter the name of the scan output file: ")

    # Run Nmap scan and save the output
    run_nmap_scan(scan_type, network_range, output_file)

