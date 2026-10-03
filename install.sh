#!/bin/sh

echo "========================================"
echo "           ZALZALA INSTALLER"
echo "========================================"
echo "Made by Pakistan ORAKXAI Anonymous"
echo

if ! command -v python3 >/dev/null 2>&1; then
    echo "[-] Python3 is not installed."
    echo "[!] Install Python3 using your system package manager."
    exit 1
fi

echo "[+] Python3 found:"
python3 --version

chmod +x zalzala.py

echo
echo "[+] ZalZala installation completed."
echo
echo "Run:"
echo "    python3 zalzala.py --help"
echo
