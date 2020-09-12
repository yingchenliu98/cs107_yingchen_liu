#!/bin/bash
grep -c '[0-9]' apollo13.txt >> apollo_out.txt
grep --help | grep -- --count
ls *.py | wc -l
find . -type f ! -perm -004 | wc -l
find . -type f ! -perm -004 -o -type d ! -perm -004 -maxdepth 1 | wc -l