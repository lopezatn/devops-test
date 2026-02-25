#!/bin/bash

# this script purpose is to check if a file exists or not.
# Works with fail-triggers

set -e
set -u
set -o pipefail

path="${1:-}"

if [ -z "$path" ]; then echo "Missing arguments"
fi
exit 1

if [ -f "$path" ]; then echo "FILE FOUND" 
else echo "FILE NOT FOUND" 
fi
