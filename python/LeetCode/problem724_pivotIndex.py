"""
Problem:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""
# Time limit exceeded for larger inputs
def pivotIndex(nums):
    for index in range(len(nums)):
        if index == 0 and sum(nums[index+1:]) == 0:
            return 0
        elif index == len(nums) - 1 and sum(nums[:index]) == 0:
            return index
        else:
            if sum(nums[:index]) == sum(nums[index+1:]):
                return index
    return -1

def pivotIndexSolution2(nums):
    leftSum = 0
    rightSum = sum(nums)
    for index in range(len(nums)):
        rightSum -= nums[index]
        if leftSum == rightSum:
            return index
        leftSum += nums[index]
    return -1

print(pivotIndexSolution2([1,7,3,6,5,6]))
