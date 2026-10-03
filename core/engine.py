from urllib.parse import urlparse

from modules.web import analyze


class ZalZalaEngine:

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

        return bool(parsed.hostname)

    def start(self):

        print("\n[+] ZalZala engine started")

        if not self.validate_target():
            print("[-] Invalid target")
            return

        target = self.normalize_target()

        print(f"[+] Target : {target}")
        print("[+] Status : SCANNING")
        print()

        print("[*] Running HTTP analysis...")

        result = analyze(target)

        print()
        print("────────────────────────────────")
        print("        HTTP ANALYSIS")
        print("────────────────────────────────")

        if "error" in result:
            print(f"[-] Error       : {result['error']}")
            return

        print(f"[+] Status      : {result['status']}")
        print(f"[+] Final URL   : {result['final_url']}")
        print(f"[+] Server      : {result['server']}")
        print(f"[+] Content-Type: {result['content_type']}")
        print(f"[+] Page Title  : {result['title']}")

        print()
        print("[+] Response Headers")

        for key, value in result["headers"].items():
            print(f"    {key}: {value}")

        print()
        print("[+] HTTP analysis completed.")
