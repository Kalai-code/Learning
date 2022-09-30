"""
Input: n = 6
a = {1, 5, 0, 3, 4, 5}
Output: -1 1 -1 0 3 4
Explaination: Upto 3 it is easy to see 
the smaller numbers. But for 4 the smaller 
numbers are 1, 0 and 3. But among them 3 
is closest. Similary for 5 it is 4.
"""

def leftSmaller(n, a):
    # code here
    output_list =[]
    for i in range(n):
        if i == 0:
            output_list.append(-1)          
        else:
            count = i
            for num in range(count,0,-1):
                if a[i] > a[num-1]:
                    output_list.append(a[num-1])
                    continue
                elif num - 1 == 0:
                    output_list.append(-1)               
                    
    print(output_list)


leftSmaller(n = 3,a = [1,6,2])

