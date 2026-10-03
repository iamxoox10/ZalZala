#!/bin/sh

echo "=========================================="
echo "            ZALZALA UPDATE"
echo "=========================================="
echo "Made by Pakistan ORAKXAI Anonymous"
echo

if ! command -v git >/dev/null 2>&1
then
    echo "[-] Git is required."
    exit 1
fi

git pull

echo
echo "[+] ZalZala updated."