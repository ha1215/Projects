#!/usr/bin/env python3
# Hassan Alshehri
# 10/05/2023
import os
import platform

def gather_system_information():
    # Get system hostname
    hostname = platform.node()

    # Get operating system information
    os_info = platform.system() + " " + platform.release()

    # Get RAM information using the free command
    ram_info = os.popen("free -h").read()

    # Get network information using ip, netstat, and ip route commands
    network_info = os.popen("ip a; netstat -rn").read()

    # Get DNS information from /etc/resolv.conf
    dns_info = open("/etc/resolv.conf").read()

    # Get system disk information using the df command
    disk_info = os.popen("df -h").read()

    # Get CPU information from /proc/cpuinfo
    cpu_info = open("/proc/cpuinfo").read()

    # Create the report
    report = f"Hostname: {hostname}\nOperating System: {os_info}\n\n"
    report += f"RAM Information:\n{ram_info}\n\n"
    report += f"Network Information:\n{network_info}\n\n"
    report += f"DNS Information:\n{dns_info}\n\n"
    report += f"Disk Information:\n{disk_info}\n\n"
    report += f"CPU Information:\n{cpu_info}"

    return report

if __name__ == "__main__":
    # Gather system information
    system_info = gather_system_information()

    # Get the hostname
    hostname = platform.node()

    # Create the filename for the log
    filename = f"/home/student/{hostname}_system_report.log"

    # Write the report to the log file
    with open(filename, "w") as file:
        file.write(system_info)

    # Print a message indicating the report has been saved
    print(f"System report saved to {filename}")
