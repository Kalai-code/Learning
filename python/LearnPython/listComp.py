#print multiples of 5 from 0 to 25
list_multiple = [x * 5 for x in range(6)]
print("Multiples of 5 from 0 to 25: " , list_multiple)

#list comprehension with if condition
list_oddnum = [x for x in range(10) if x % 2 != 0]
print("Odd numbers: " , list_oddnum)

#list matrix
list_matrix = [[i,j] for i in range(1,5) for j in range(1,3)]
print("List matrix: ", list_matrix)

#list split
list_words = 'Hello there'
list_split = [ch for ch in list_words]
print("Split the List: ", list_split)
print(list(list_words))

#lambda expression - square of the numbers
list_lambda = [x ** 2 for x in range(6)]
print("Lambda Example: ", list_lambda)

# sum of digits of elements in the list
def sumOfDigits(num):
    totalSum = 0
    while num > 0:
        totalSum += num % 10
        num = num // 10
    return totalSum

list_numbers = [367,111,562,945,6726,873]
list_digitSum = [sumOfDigits(i) for i in list_numbers]
print("Sum of Digitis of elements in the list: ", list_digitSum)
