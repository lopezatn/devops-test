import subprocess

usage = subprocess.run(["df", "-h" ,"/"], capture_output=True, text=True).stdout
usage = int(usage.splitlines()[1].split()[4].strip("%"))

if usage > 80:
    print(f"WARNING: disk usage is at {usage}%")
    exit(1)
else:
    print(f"OK: Disk usage is at {usage}%")
    exit()
