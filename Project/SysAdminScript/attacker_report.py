#! /usr/bin/env python3
# Student Name: Hassan Alshehri
# Date: 11/9/2023

import re
from geoip import geolite2
from datetime import datetime
import os
import sys

os.system('clear')


def get_country(ip):
    match = geolite2.lookup(ip)
    return match.country if match else 'Unknown'

def parse_logs(logfile_path):
    with open(logfile_path, 'r') as file:
        logs = file.read()

    # Regex pattern to match IP addresses and failed attempts
    pattern = re.compile(r'Failed password for .+ from (\S+)')
    failed_attempts = re.findall(pattern, logs)

    # Count failed attempts per IP
    attempt_counts = {ip: failed_attempts.count(ip) for ip in set(failed_attempts)}
    return attempt_counts

def generate_report(attempt_counts):
    print(f'Attacker Report: {datetime.now().strftime("%d-%m-%Y %H:%M")}\n')
    print(f'{"IP Address":<20}{"Count":<15}{"Country":<15}')


    # Filter and sort the IPs with 10 or more failed attempts
    filtered_attempts = {ip: count for ip, count in attempt_counts.items() if count >= 10}
    for ip in sorted(filtered_attempts, key=filtered_attempts.get):
        print(f'{ip:<20}{filtered_attempts[ip]:<15}{get_country(ip):<15}')

if __name__ == '__main__':
    # Assume syslog.log is in the same directory as the script
    log_path = '/home/student/Desktop/syslog.log'
    if not os.path.exists(log_path):
        print("syslog.log file not found in the expected directory.")
        sys.exit(1)

    attempts = parse_logs(log_path)
    generate_report(attempts)

