#! /usr/bin/bash

#for loop
sentence="Welcome to the world of learning"
for word in $sentence
do
    echo $word
done
echo "\n"
echo "Numbers 1 to 10"
for num in {1..10}
do
    echo $num
done

num1=10
num2=20
num3=$(($num1 + $num2))
echo "Sum of 10 and 20 is $num3"
