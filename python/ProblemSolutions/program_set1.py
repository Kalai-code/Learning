"""
Problems:
1. Calculate the sum of the digits
2. Reverse integer
3. Check if a number is palindrome or not
"""

def number_Sum(num):
    totalSum = 0
    while num > 0:
        totalSum += num % 10
        num = num // 10
    return totalSum

print("Sum of digits: ")
print("Input: ", str(12345))
print("Output: ", number_Sum(12345))


def reverse_integer(num):
    revNum = 0
    while num > 0:
        revNum = revNum * 10 + num % 10
        num = num // 10
    return revNum

print("Reverse Number: ")
print("Input: ", str(1234))
print("Output: ", reverse_integer(1234))


def num_palindrome(num):
    oldNum,palNum = num,0
    if num < 0:
        return False
    else:
        while oldNum > 0:
            palNum = palNum * 10 + oldNum % 10
            oldNum = oldNum // 10
        if num == palNum:
            return True
        else:
            return False


print("Palindrome Number or Not: ")
print("Input: ", str(1234))
print("Output: ", num_palindrome(1234))

print("Palindrome Number or Not: ")
print("Input: ", str(1221))
print("Output: ", num_palindrome(1221))

