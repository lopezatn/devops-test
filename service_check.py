import sys, subprocess

try:
    service = sys.argv[1]
except IndexError:
    print("Missing parameters, please try again")
    exit(1)

is_active = subprocess.run(["systemctl", "is-active", service], capture_output = True).returncode

if is_active == 0:
    print(f"OK: {service} is running")
    exit(0)
else:
    print(f"CRITICAL: {service} is not running")
    exit(1)
