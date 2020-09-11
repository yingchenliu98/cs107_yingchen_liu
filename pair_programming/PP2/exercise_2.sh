#!/bin/bash
# Section Friday, Week 2 Pair Programming
# listener: Michelle Owens, Chen (Lucy) Zhang
# coder: Chen (Lucy) Zhang, Michelle Owens, Yingchen Liu

for file in $(find . -type f)
do
    if [ -x $file ]; then
        echo $file
    fi
done