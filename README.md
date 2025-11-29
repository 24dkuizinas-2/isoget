# isoget

**isoget** is a lightweight, cross‑platform command‑line utility for installing ISO images onto removable devices.  
It provides a simple, safe, and consistent interface for writing `.iso` files to USB sticks or external drives across all major Linux distributions.

---

## ✨ Features
- Universal ISO support: Works with any `.iso` file, not tied to a specific distribution.
- Cross‑distro packaging: Available for Debian/Ubuntu/Mint (`apt`) atm, will support more systems later on.
- Device detection: Lists available block devices so you can safely choose your USB stick.
- Checksum verification: Optional SHA256 integrity checks before writing.
- Minimal dependencies: Built in Python for portability, with no heavy runtime overhead.

---

## 📦 Installation

### Debian / Ubuntu / Mint
```bash
sudo apt install isoget.deb
sudo isoget -i /root/etc/isofiles/pylynx.iso
```

## 🚀 Usage
## Install an ISO to a USB device
```bash
sudo isoget -i /path/to/example.iso -d /dev/sdX
```
### -i → Path to the ISO file

### -d → Target device (e.g. /dev/sdb for a USB stick)

```bash List available devices
isoget -l
Verify ISO checksum
isoget -i /path/to/example.iso --verify sha256sum.txt
```
## ⚠️ Safety Notes
### Always double‑check the target device (/dev/sdX) before writing.

### Writing an ISO will erase all data on the target device.

### Use isoget -l to confirm which device is your USB stick.

## 🛠️ Development
## Written in Python for portability.

### Packaged for multiple Linux distributions.

#### Contributions welcome: fork, patch, and submit pull requests.

