import sys, json

try:
    json_file = open(sys.argv[1])
except (FileNotFoundError, IndexError):
    print("JSON File is missing, try again")
    exit(1)

config = json.load(json_file)
key_list = []


for key in ["host", "port", "environment"]:
    if key not in config:
        print(f"MISSING KEY: {key}")
        exit(1)
    else:
        key_list.append(key)

for key in key_list:
    print(f"{key}: {config[key]}")
