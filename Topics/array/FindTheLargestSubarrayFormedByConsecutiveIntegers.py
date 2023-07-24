"""
    Given an integer array, find the largest subarray formed by consecutive integers. The subarray should contain all distinct values.
    
    Example:-
    Input:  [2, 0, 2, 1, 4, 3, 1, 0]
 
    Output: The largest subarray is [0, 2, 1, 4, 3]

"""

def largestSubarray(nums):
    
    if len(nums) == 1:
        return nums[0]
    
    total = nums[0]
    best = nums[0]
    
    for i in nums[1:]:
        if i > (total + 1):
            total = i
        else:
            total += i
            
        best = max(best, total)
        
    return best
    
if __name__ == "__main__":
    
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    print(largestSubarray(nums))