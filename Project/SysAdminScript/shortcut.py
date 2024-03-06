#!/usr/bin/env python3

#Hassan Alshehri
#10/25/2023
import os
from pathlib import Path
import subprocess

# Define the path to the user's Desktop
DESKTOP_PATH = Path.home() / 'Desktop'

#Function to clear the terminal screen
def clear_screen():
    os.system('clear')

#Function to display the main menu to the user and get thir choice
def get_menu_choice():
    clear_screen()
    print(f"Current Working Directory: {os.getcwd()}")
    print("\nShortcut Menu:")
    print("1. Create a symbolic link")
    print("2. Delete a symbolic link")
    print("3. Generate a report of symbolic links")
    print("Type 'quit' to exit")
    return input("\nYour choice: ")

#Function to creat a symbolic link on the users Desktop
def create_symbolic_link():
    source_file = input("Enter the path to the file you want to create a shortcut for: ")
    source_path = Path(source_file)
    if not source_path.exists():
        print(f"\nThe file '{source_file}' does not exist!")
        input("Press Enter to continue...")
        return
    link_name = input("Enter the name for the symbolic link (without path): ")
    link_path = DESKTOP_PATH / link_name
    os.symlink(source_path, link_path)
    print(f"\nSymbolic link '{link_name}' created on Desktop!")
    input("Press Enter to continue...")

#Function to delete a symbolic link from the users Desktop
def delete_symbolic_link():
    link_name = input("Enter the name of the symbolic link you want to delete (from Desktop): ")
    link_path = DESKTOP_PATH / link_name
    if not link_path.is_symlink():
        print(f"\nThe file '{link_name}' is not a symbolic link on Desktop!")
        input("Press Enter to continue...")
        return
    os.unlink(link_path)
    print(f"\nSymbolic link '{link_name}' deleted!")
    input("Press Enter to continue...")

#Function to generate a report of all symbolic links on the users Desktop
def generate_report():
    links = [link for link in DESKTOP_PATH.iterdir() if link.is_symlink()]
    if not links:
        print("\nNo symbolic links found on Desktop!")
    else:
        print("\nSymbolic Links Report:")
        for link in links:
            target = os.readlink(link)
            print(f"{link.name} -> {target}")
        print(f"\nTotal number of symbolic links on Desktop: {len(links)}")
    input("Press Enter to continue...")

#Main function that drives the script
def main():
    while True:
        choice = get_menu_choice()
        if choice == '1':
            create_symbolic_link()
        elif choice == '2':
            delete_symbolic_link()
        elif choice == '3':
            generate_report()
        elif choice.lower() == 'quit':
            clear_screen()
            break
        else:
            print("\nInvalid choice! Try again.")
            input("Press Enter to continue...")

#Entry point for the script
if __name__ == '__main__':
    main()
