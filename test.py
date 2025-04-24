import subprocess

try:
    version = subprocess.check_output(["gswin64c", "--version"], text=True)
    print("Ghostscript version:", version.strip())
except FileNotFoundError:
    print("Ghostscript NOT found in PATH!")
except Exception as e:
    print("Ghostscript error:", e)
