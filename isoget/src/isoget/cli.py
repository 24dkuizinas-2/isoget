import argparse
from . import core

def main():
    parser = argparse.ArgumentParser(
        description="isoget — Universal ISO installer"
    )
    parser.add_argument(
        "-i", "--iso",
        help="Path to ISO file"
    )
    parser.add_argument(
        "-d", "--device",
        help="Target device (e.g. /dev/sdb)"
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List available block devices"
    )
    parser.add_argument(
        "--verify",
        help="Optional checksum file (SHA256)"
    )

    args = parser.parse_args()

    if args.list:
        core.list_devices()
    elif args.iso and args.device:
        core.write_iso(args.iso, args.device, args.verify)
    else:
        parser.print_help()
