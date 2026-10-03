#!/bin/sh

echo "=========================================="
echo "          ZALZALA INSTALLER"
echo "=========================================="
echo "Made by Pakistan ORAKXAI Anonymous"
echo

if ! command -v python3 >/dev/null 2>&1
then
    echo "[-] Python3 is required."
    echo "[!] Install it with:"
    echo "    apk add python3"
    exit 1
fi

chmod +x zalzala.py

echo "[+] Python3:"
python3 --version

echo
echo "[+] ZalZala installed."
echo
echo "Run:"
echo "    python3 zalzala.py --help"