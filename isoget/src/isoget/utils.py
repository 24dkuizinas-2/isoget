import os
import hashlib

def verify_checksum(file_path, checksum_file):
    """Verify SHA256 checksum of ISO against checksum file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    calculated = sha256.hexdigest()

    with open(checksum_file, "r") as cf:
        expected = cf.read().strip().split()[0]

    if calculated == expected:
        print("Checksum verified successfully.")
        return True
    else:
        print(f"Checksum mismatch!\nExpected: {expected}\nGot: {calculated}")
        return False

def get_file_size(file_path):
    """Return file size in bytes."""
    return os.path.getsize(file_path)
