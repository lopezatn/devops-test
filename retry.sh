#!/bin/bash

for i in 1 2 3
do
	echo "Attempt number ${i}"
	$1
	if [ $? == 0 ]; then
		exit
	fi
done

exit 1
