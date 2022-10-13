from itertools import count


numList = [1,2,2,3,3,3]

num = [x for x in numList if numList.count(x) > 1]

print(num)