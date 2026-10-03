from urllib.parse import urlparse


class ZalZalaEngine:
    """
    Core engine for ZalZala.

    Made by Pakistan ORAKXAI Anonymous
    """

    def __init__(self, target):
        self.target = target

    def normalize_target(self):
        target = self.target.strip()

        if not target.startswith(("http://", "https://")):
            target = "https://" + target

        return target.rstrip("/")

    def validate_target(self):
        target = self.normalize_target()
        parsed = urlparse(target)

        if not parsed.hostname:
            return False

        return True

    def start(self):
        print("\n[+] ZalZala engine started")

        if not self.validate_target():
            print("[-] Invalid target")
            return

        target = self.normalize_target()

        print(f"[+] Target : {target}")
        print("[+] Status : READY")
        print()
        print("[*] Recon modules will be loaded here.")
        print("[*] Use only on systems you own or are authorized to test.")
