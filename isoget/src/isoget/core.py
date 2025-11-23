import subprocess
import shutil
import hashlib
from . import utils

def list_devices():
    """List block devices using lsblk."""
    subprocess.run(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINT"])

def write_iso(iso_path, device, checksum_file=None):
    """Write ISO to target device, with optional checksum verification."""
    try:
        # Unmount device before writing
        subprocess.run(["umount", device], stderr=subprocess.DEVNULL)

        # Verify checksum if provided
        if checksum_file:
            if not utils.verify_checksum(iso_path, checksum_file):
                print("Checksum verification failed!")
                return

        # Stream ISO to device
        with open(iso_path, "rb") as iso, open(device, "wb") as dev:
            shutil.copyfileobj(iso, dev)
            print(f"ISO {iso_path} written to {device}")

    except Exception as e:
        print(f"Error writing ISO: {e}")
