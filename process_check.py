import sys, subprocess

processname = sys.argv[1]

isprocessrunning = subprocess.run(["pgrep", processname], capture_output=True)

if isprocessrunning.returncode == 0:
    print(f"Process {processname} is running")
else:
    print(f"Process {processname} is not running")


