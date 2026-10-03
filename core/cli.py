import argparse

from core.banner import show_banner
from core.engine import ZalZalaEngine


def run():
    parser = argparse.ArgumentParser(
        prog="zalzala",
        description="ZalZala Security Recon Framework"
    )

    parser.add_argument(
        "-u",
        "--url",
        help="Authorized target URL/domain"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Run full security assessment"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ZalZala 1.0.0"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show framework information"
    )

    args = parser.parse_args()

    show_banner()

    if args.info:
        print("Name     : ZalZala")
        print("Version  : 1.0.0")
        print("Author   : Pakistan ORAKXAI Anonymous")
        print("Platform : Linux / Termux / iSH")
        return

    if not args.url:
        parser.print_help()
        return

    engine = ZalZalaEngine(args.url)

    if args.full:
        engine.full_scan()
    else:
        engine.web_scan()
