import argparse

from core.banner import show_banner
from core.engine import ZalZalaEngine


def build_parser():
    parser = argparse.ArgumentParser(
        prog="zalzala",
        description="ZalZala Security Recon Framework"
    )

    parser.add_argument(
        "-u",
        "--url",
        help="Authorized target URL"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ZalZala 0.1.0"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show framework information"
    )

    return parser


def run():
    show_banner()

    parser = build_parser()
    args = parser.parse_args()

    if args.info:
        print("ZalZala Security Recon Framework")
        print("Version : 0.1.0")
        print("Author  : Pakistan ORAKXAI Anonymous")
        print("Platform: Linux / Termux / iSH")
        return

    if args.url:
        engine = ZalZalaEngine(args.url)
        engine.start()
        return

    parser.print_help()
