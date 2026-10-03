cd ~/ZalZala
cat > core/cli.py <<'PY'
import argparse

from core.banner import show_banner
from core.engine import ZalZalaEngine

VERSION = "1.0.0"


def build_parser():
    parser = argparse.ArgumentParser(
        prog="zalzala",
        description="ZalZala Security Recon Framework"
    )

    parser.add_argument(
        "-u", "--url",
        help="Authorized target URL/domain"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Run full security assessment"
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
        help="Check security headers"
    )

    parser.add_argument(
        "--tls",
        action="store_true",
        help="Analyze TLS configuration"
    )

    parser.add_argument(
        "--cms",
        action="store_true",
        help="Detect CMS/technologies"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ZalZala {VERSION}"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show framework information"
    )

    return parser


def show_info():
    print()
    print("ZalZala Security Recon Framework")
    print("=" * 45)
    print(f"Version : {VERSION}")
    print("Author  : Pakistan ORAKXAI Anonymous")
    print()
    print("For authorized security assessments,")
    print("CTFs and laboratory environments.")
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

    engine = ZalZalaEngine(args.url)

    if args.full:
        engine.full_scan()
        return

    # Current engine has a complete web_scan method.
    # Individual module execution will be added through
    # the engine as the framework expands.
    if args.web or not any([
        args.dns,
        args.headers,
        args.tls,
        args.cms
    ]):
        engine.web_scan()
        return

    # For now, --full is the supported multi-module mode.
    print("[!] Individual module mode is not yet connected.")
    print("[!] Use --full for the complete assessment.")


if __name__ == "__main__":
    run()
PY