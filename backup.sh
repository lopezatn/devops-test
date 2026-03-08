#!/bin/bash

if [ -z $1 ] || [ -z $2 ]; then
	echo "One or more arguments are missing, please try again"
	exit 1
else
	if [ ! -d $1 ]; then
		echo "Source directory not found"
		exit 1
	fi
fi

source=$1
destination=$2.$(date +%Y-%m-%d)


mv ${source} ${destination}
echo "The backup was successfully done, destination is: ${destination}"
