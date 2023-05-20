import subprocess
import sys
import contextlib

def install(package):

    subprocess.call(sys.executable, '-m', 'pip', 'install', package)


required = []
failed = []

try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No requiremnts.txt file found")


if len(required) > 0:
    print("[INPUT] You are about to install", len(required), "packages, would you like to proceed (y/n):", end=" ")
    ans = input()

    if ans.lower() == "y":
        for package in required:
            try:
                print("[LOG] Looking for", package)
                with contextlib.redirect_stdout(None):
                    __import__(package)
                print("[LOG]", package, "is already installed, skipping...")
            except ImportError:
                print("[LOG]", package, "not installed")

                try:
                    print("[LOG] Trying to install", package, "via pip")
                    try:
                        import pip
                    except:
                        print("[EXCEPTION] Pip is not installed")
                        print("[LOG] You need to install pip first and try again")
                except Exception as e:
                    print("[ERROR] Could not install", package, "-", e)
                    failed.append(package)
    else:
        print("[STOP] Operation terminated by user")
else:
    print("[LOG] No packages to install")

if len(failed) > 0:
    print("[FAILED]", len(failed), "package(s) were not installed. Failed package install(s):", end=" ")
    for x, package in enumerate(failed):
        if x != len(failed) -1:
            print(package, end=",")
        else:
            print(package)