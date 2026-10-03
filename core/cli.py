import argparse

from core.engine import run_scan
from core.banner import show_banner


VERSION = "1.0.0"


def build_parser():
    parser = argparse.ArgumentParser(
        prog="zalzala",
        description="ZalZala - Security Assessment & Recon Tool"
    )

    parser.add_argument(
        "-u", "--url",
        help="Target URL or domain"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Run all available assessment modules"
    )

    parser.add_argument(
        "--web",
        action="store_true",
        help="Run web analysis"
    )

    parser.add_argument(
        "--dns",
        action="store_true",
        help="Run DNS analysis"
    )

    parser.add_argument(
        "--headers",
        action="store_true",
        help="Check HTTP security headers"
    )

    parser.add_argument(
        "--tls",
        action="store_true",
        help="Analyze TLS/SSL configuration"
    )

    parser.add_argument(
        "--ports",
        action="store_true",
        help="Check common TCP ports"
    )

    parser.add_argument(
        "--subdomains",
        action="store_true",
        help="Check common subdomains"
    )

    parser.add_argument(
        "--cms",
        action="store_true",
        help="Detect common CMS/frameworks"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ZalZala {VERSION}"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show information about ZalZala"
    )

    return parser


def show_info():
    print()
    print("ZalZala")
    print("=" * 45)
    print("Security Assessment & Recon Tool")
    print(f"Version : {VERSION}")
    print("Author  : Pakistan ORAKXAI Anonymous")
    print()
    print("Designed for authorized security testing,")
    print("CTFs, labs, and systems you have permission to test.")
    print()


def run():
    parser = build_parser()
    args = parser.parse_args()

    if args.info:
        show_info()
        return

    if not args.url:
        show_banner()
        parser.print_help()
        return

    modules = []

    if args.full:
        modules = [
            "web",
            "dns",
            "headers",
            "tls",
            "ports",
            "subdomains",
            "cms",
        ]
    else:
        if args.web:
            modules.append("web")

        if args.dns:
            modules.append("dns")

        if args.headers:
            modules.append("headers")

        if args.tls:
            modules.append("tls")

        if args.ports:
            modules.append("ports")

        if args.subdomains:
            modules.append("subdomains")

        if args.cms:
            modules.append("cms")

    # If only URL is supplied, run the basic web assessment.
    if not modules:
        modules = ["web"]

    try:
        run_scan(args.url, modules)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    except Exception as exc:
        print(f"\n[!] Error: {exc}")


if __name__ == "__main__":
    run()