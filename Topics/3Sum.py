"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]], 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example:-
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = []
    Output: []

    Input: nums = [0]
    Output: []
    
"""
def threeSum(self, nums):
    res = []
    nums.sort()
        
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
                
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1    
    return res