import subprocess
import hashlib
from tqdm import tqdm
from . import utils

def list_devices():
    """List block devices using lsblk."""
    subprocess.run(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINT"])

def write_iso(iso_path, device, checksum_file=None):
    """Write ISO to target device, with optional checksum verification and progress bar."""
    try:
        # Unmount device before writing
        subprocess.run(["umount", device], stderr=subprocess.DEVNULL)

        # Verify checksum if provided
        if checksum_file:
            if not utils.verify_checksum(iso_path, checksum_file):
                print("Checksum verification failed!")
                return

        # Get ISO size for progress bar
        iso_size = utils.get_file_size(iso_path)

        # Stream ISO to device with progress bar
        with open(iso_path, "rb") as iso, open(device, "wb") as dev:
            with tqdm(total=iso_size, unit="B", unit_scale=True, desc="Writing ISO") as pbar:
                for chunk in iter(lambda: iso.read(1024 * 1024), b""):
                    dev.write(chunk)
                    pbar.update(len(chunk))

        print(f"ISO {iso_path} written to {device}")

    except Exception as e:
        print(f"Error writing ISO: {e}")
