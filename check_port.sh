#!/bin/bash

set -e
set -u
set -o pipefail

isListening=$(ss -tnlp | grep $1) || true

if ss -tnlp | grep -q $1; then
	echo "Port $1 is in use by: $isListening"
else
	echo "Port $1 is not in use"
fi
