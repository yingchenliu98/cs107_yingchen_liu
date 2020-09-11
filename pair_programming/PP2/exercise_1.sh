#!/bin/bash
# Section Friday, Week 2 Pair Programming

# listener: Chen (Lucy) Zhang
# coder: Yingchen Liu
# sharer: Michelle Owens

read -r -p "Input the file name" filename

git add $filename

git status

read -r -p "Do you wish to continue?[Y/N]" answer1

if [ "$answer1" =  "N" ]; then 

    exit 1

elif [ "$answer" = "Y" ]; then

        read -r -p "Give the commit message: " message

        git commit -m "$message"

        git status
fi

read -r -p "Do you wish to continue?[Y/N]" answer2

if [ "$answer2" =  "N" ]; then 

    exit 1

elif

    git push
fi