"""
isoget — Universal ISO installer
"""

__version__ = "0.1.0"

# Expose main functions at package level if needed
from .cli import main
from .core import list_devices, write_iso
