#!/bin/bash

set -e
set -u
set -o pipefail

usage=$(df -h / | awk 'NR==2 {print $5}' |tr -d '%')

if [ "$usage" -gt 80 ]; then
  echo "WARNING: Disk usage is at $usage%"
else
  echo "Disk usage is OK: $usage%"
fi

