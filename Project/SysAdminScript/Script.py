#!/usr/bin/python3

# Hassan Alshehri
# 09/23/2023

#it worked in my machine but i don't know why the shebang is not working here. otherwise every thing is working
import os

def display_gateway():
    try:
        gateway = os.popen('ip r | awk \'/default/ {print $3}\'').read().strip()
        print(f"Default Gateway: {gateway}")
    except Exception as e:
        print(f"Error retrieving default gateway: {str(e)}")

def test_local_connectivity():
    try:
        local_ip = '127.0.0.1'
        response = os.system(f'ping -c 1 {local_ip}')
        if response == 0:
            print(f"Local Connectivity Test to {local_ip}: Successful")
        else:
            print(f"Local Connectivity Test to {local_ip}: Failed")
    except Exception as e:
        print(f"Error testing local connectivity: {str(e)}")

def test_remote_connectivity():
    try:
        remote_ip = '129.21.3.17'
        response = os.system(f'ping -c 1 {remote_ip}')
        if response == 0:
            print(f"Remote Connectivity Test to {remote_ip}: Successful")
        else:
            print(f"Remote Connectivity Test to {remote_ip}: Failed")
    except Exception as e:
        print(f"Error testing remote connectivity: {str(e)}")

def test_dns_resolution():
    try:
        url = 'www.google.com'
        response = os.system(f'ping -c 1 {url}')
        if response == 0:
            print(f"DNS Resolution Test for {url}: Successful")
        else:
            print(f"DNS Resolution Test for {url}: Failed")
    except Exception as e:
        print(f"Error testing DNS resolution: {str(e)}")

def main():
    while True:
        print("\nMenu:")
        print("1. Display the default gateway")
        print("2. Test Local Connectivity")
        print("3. Test Remote Connectivity")
        print("4. Test DNS Resolution")
        print("5. Exit/quit the script")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_gateway()
        elif choice == '2':
            test_local_connectivity()
        elif choice == '3':
            test_remote_connectivity()
        elif choice == '4':
            test_dns_resolution()
        elif choice == '5':
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
