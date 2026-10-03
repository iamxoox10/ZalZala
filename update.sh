#!/bin/sh

echo "========================================"
echo "            ZALZALA UPDATE"
echo "========================================"
echo "Made by Pakistan ORAKXAI Anonymous"
echo

if command -v git >/dev/null 2>&1; then
    git pull
else
    echo "[-] Git is not installed."
    exit 1
fi

echo
echo "[+] Update process completed."
