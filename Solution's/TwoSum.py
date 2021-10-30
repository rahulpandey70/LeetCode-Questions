"""
                Given an array of integers nums and an integer target, 
                return indices of the two numbers such that they add up to target.
                You may assume that each input would have exactly one solution, and you may not use the same element twice.
                You can return the answer in any order.

                Example:-

                Input: nums = [2,7,11,15], target = 9
                Output: [0,1]
                Output: Because nums[0] + nums[1] == 9, we return [0, 1].

                Input: nums = [3,2,4], target = 6
                Output: [1,2]

                Input: nums = [3,3], target = 6
                Output: [0,1]

"""

# Solution 1.
def twoSum(self, nums, target):
    for i, n in enumerate(nums):
        try:
            r1 = nums.index(target-n)
        except:
            continue
        if r1 != i:
            return [i,r1]

# Solution 2.
def twoSum(self, nums, target):      
    prev = {} 
    for i, n in enumerate(nums):
        diff = target - n    
        if diff in prev:
            return [prev[diff], i]
        prev[n] = i        
    return
        