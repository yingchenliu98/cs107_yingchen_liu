#!/bin/bash
# counts and prints the number of lines of each file in the current director with its name
result=`ls -p | grep -v /`
for file in $result
do
	echo "$file" `wc -l < $file`
done

