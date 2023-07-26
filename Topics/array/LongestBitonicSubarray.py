"""
    Longest Bitonic Subarray Problem
    
    The Longest Bitonic Subarray (LBS) problem is to find a subarray of a given sequence in which the subarray's elements are first sorted in increasing order, then in decreasing order, and the subarray is as long as possible. Strictly ascending or descending subarrays are also accepted.
    
    Example:-
    
    nums = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    
    Longest bitonic subarray of the sequence is [4, 5, 9, 10, 8, 5, 3]

"""

def findBitonicSubarray(nums):
    
    n = len(nums)
    
    # base case
    if n == 0:
        return
    
    endingIndex = 0
    maxLen = 1
    i = 0
    
    while i + 1 < n:
        
        # reset length
        length = 1
        
        # run till sequence is increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i = i + 1
            length = length + 1
        
        # run till sequence is decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i = i + 1
            length = length + 1
        
        # run till sequence is equal
        while i + 1 < n and nums[i] == nums[i + 1]:
            i = i + 1
            
        # update longest bitonic subarray
        if length > maxLen:
            maxLen = length
            endingIndex = i
    
    # print
    print("Bitonic subarray length is:", maxLen)
    print("Longest bitonic subarray is:", nums[endingIndex - maxLen + 1: endingIndex + 1])
    
if __name__ == "__main__":
    
    nums = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    findBitonicSubarray(nums)