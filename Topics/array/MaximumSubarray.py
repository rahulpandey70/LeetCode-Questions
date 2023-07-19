"""
    Given an integer array nums, find the contiguous subarray (containing at least one number), 
    which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    Example:-
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Input: nums = [5,4,-1,7,8]
    Output: 23

    Input: nums = [1]
    Output: 1
"""
def maxSubArray(self, nums):
    maxSub = nums[0]
    currSum = 0
        
    for i in nums:
        if currSum < 0: # Checking if currSum is at any point negative, reset the value of currSum with 0.
            currSum = 0
        currSum += i
        maxSub = max(maxSub, currSum)
    return maxSub