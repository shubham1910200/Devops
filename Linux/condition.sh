#!/bin/bash

echo "Enter a number"
read number
if [ $number -gt 10 ]
then 
    echo "The number is greater than ten"
else 
    echo "The number is less than ten"
fi
