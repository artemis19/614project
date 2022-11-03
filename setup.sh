#!/bin/bash

if [ "$UID" -eq "0" ]; then
	echo "[!] This script should NOT be run directly as root. Exiting..."
	exit
fi

echo "[+] This script needs root permissions to perform certain tasks."
sudo true

# Update repos
sudo apt update

# Install VSCode
sudo apt install code

# Install xautomation
sudo apt install xautomation