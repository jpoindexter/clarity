import sys
import os

# ✅ Force pytest to recognize `src` as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
