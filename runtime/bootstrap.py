import sys
import os

def bootstrap():
    # Force repo root into Python path
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)

    print("✔ Runtime bootstrap loaded")
