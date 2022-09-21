import copy

original_list = [1,2,3,[4,5,6]]

# using = operator copies the entire list. When change is made to the original list, the change is reflected in equalList
equalList = original_list
shallowcopy1 = original_list[:]
shallowcopy2 = copy.copy(original_list)
deepCopy = copy.deepcopy(original_list)

print("List Before Modification:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

original_list[3][0] = 10

print("List After Modifying Inner List:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

original_list[0] = 11

print("List After Modifying Inner List and Outer List:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

equalList[3][1] = 12

print("List After Modifying Equal List:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

shallowcopy1[3][2] = 13
shallowcopy1[0] = 20

print("List After Modifying Shallow Copy1:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

shallowcopy2[3][0] = 14

print("List After Modifying Shallow Copy2:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

deepCopy[0] = 15

print("List After Modifying Deep Copy Outer List:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")

deepCopy[3][0] = 16

print("List After Modifying Deep Copy Inner List:")

print("Original list: ", original_list)
print("List after using equal sign: ", equalList)
print("Shallow copy using : ", shallowcopy1)
print("Shallow copy using copy: ", shallowcopy2)
print("Deep copy:", deepCopy)
print("\n")


