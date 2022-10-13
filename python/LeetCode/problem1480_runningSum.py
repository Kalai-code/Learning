"""
Problem:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

def runningSum(nums):
    output = []
    for index in range(len(nums)):
        output.append(sum(nums[:index+1]))
    return output

def runningSumSolution2(nums):
    runningSum = [nums[0]]
    for i in range(1,len(nums)):
        runningSum.append(runningSum[i - 1] + nums[i])
    return runningSum

print(runningSumSolution2([1,2,3,4]))