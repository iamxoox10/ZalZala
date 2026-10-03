from urllib.parse import urlparse

from modules.web import scan_web
from modules.headers import analyze_headers
from modules.dns import analyze_dns
from modules.tls import analyze_tls
from modules.cms import detect_cms
from reports.generator import save_report


class ZalZalaEngine:

    def __init__(self, target):
        self.target = self.normalize(target)
        self.results = {}

    def normalize(self, target):
        target = target.strip()

        if not target.startswith(("http://", "https://")):
            target = "https://" + target

        return target.rstrip("/")

    def valid(self):
        parsed = urlparse(self.target)
        return bool(parsed.hostname)

    def web_scan(self):
        if not self.valid():
            print("[-] Invalid target")
            return

        print(f"\n[+] Target: {self.target}")
        print("[+] Running web analysis...\n")

        result = scan_web(self.target)
        self.results["web"] = result

        self.print_web(result)

        path = save_report(self.target, self.results)
        print(f"\n[+] Report: {path}")

    def full_scan(self):
        if not self.valid():
            print("[-] Invalid target")
            return

        print(f"\n[+] Target: {self.target}")
        print("[+] Starting full assessment\n")

        print("[1/5] Web analysis...")
        self.results["web"] = scan_web(self.target)

        print("[2/5] Security headers...")
        self.results["headers"] = analyze_headers(
            self.results["web"].get("headers", {})
        )

        hostname = urlparse(self.target).hostname

        print("[3/5] DNS analysis...")
        self.results["dns"] = analyze_dns(hostname)

        print("[4/5] TLS analysis...")
        self.results["tls"] = analyze_tls(hostname)

        print("[5/5] Technology/CMS detection...")
        self.results["cms"] = detect_cms(
            self.results["web"]
        )

        print("\n========== RESULTS ==========\n")

        self.print_web(self.results["web"])

        print("\n[+] Security Headers")
        for item in self.results["headers"]:
            print(f"    {item}")

        print("\n[+] DNS")
        for key, value in self.results["dns"].items():
            print(f"    {key}: {value}")

        print("\n[+] TLS")
        for key, value in self.results["tls"].items():
            print(f"    {key}: {value}")

        print("\n[+] Technology")
        for item in self.results["cms"]:
            print(f"    {item}")

        path = save_report(self.target, self.results)

        print("\n=============================")
        print(f"[+] Assessment complete")
        print(f"[+] Report: {path}")

    def print_web(self, result):
        print("[+] HTTP")

        for key in (
            "status",
            "final_url",
            "server",
            "content_type",
            "title"
        ):
            print(f"    {key}: {result.get(key)}")