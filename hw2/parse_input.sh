#!/bin/bash

files='test_files.txt'
inputs=''
file_num=0

while read file; do
	if (( $file_num != 0 ))
	then
		inputs+=','
	fi
	inputs+=$file
	((file_num+=1))
done < $files

echo $inputs
