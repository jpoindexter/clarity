import os


def detect_circular_imports():
    """✅ Detects circular imports in the backend directory."""
    output = os.popen(
        'python -m trace --trace backend/ 2>&1 | grep "import" | grep "circular"'
    ).read()
    if output:
        print("🚨 Circular Import Detected! 🚨")
        print(output)
        exit(1)  # ✅ Stop execution if circular imports are found
    else:
        print("✅ No circular imports detected.")


if __name__ == "__main__":
    detect_circular_imports()
