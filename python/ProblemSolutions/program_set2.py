"""
1. find if string is palindrome or not
2. find if a sentence is palindrom or not
"""

def string_palindrome(input_str):
    first_index = 0
    last_index = len(input_str) - 1
    while first_index < last_index:
        if input_str[first_index] == input_str[last_index]:
            first_index += 1
            last_index -= 1
        else:
            return False
    return True

print("Palindrome string:")
print("Input: madam")
print("Output: ", string_palindrome("madam"))
print("\n")
print("Palindrome string:")
print("Input: Noon")
print("Output: ", string_palindrome("noon"))
print("\n")
print("Palindrome string:")
print("Input: pascal")
print("Output: ", string_palindrome("pascal"))


