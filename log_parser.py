import sys

try:
    file = open(sys.argv[1])
except (FileNotFoundError, IndexError):
    print("The file argument is empty or missing")
    exit(1)

found_errors = ""
for i, line in enumerate(file):
    if "ERROR" in line:
        found_errors += f"Line {i + 1}: {line}"

if found_errors == "":
    print("No errors found")
    exit(0)
else:
    print(found_errors)
    exit(0)
