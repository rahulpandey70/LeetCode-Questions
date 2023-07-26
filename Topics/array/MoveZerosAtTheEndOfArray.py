"""
    Move all zeros present in an array to the end

    Given an integer array, move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.
    
    Example:
    
    Input:  [6, 0, 8, 2, 3, 0, 4, 0, 1]
 
    Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]
    
    1. If the current element is non-zero, place the element at the next available position in the array. After all elements in the array are processed, fill all remaining indices by 0.
    
    2. We can also solve this problem in one scan of the array by modifying Quicksort's partitioning logic. The idea is to use 0 as a pivot element and make one pass of the partition process. The partitioning logic reads all elements and swap every non-pivot element with the first occurrence of the pivot.

"""

def moveZeroAtTheEnd(nums):
    
    # index of the next available position
    k = 0
    
    for i in nums:
        if i:
            nums[k] = i
            k = k + 1
    
    # move all zero at the end of the array
    for i in range(k, len(nums)):
        nums[i] = 0
    
if __name__ == "__main__":
    
    nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    moveZeroAtTheEnd(nums)
    print(nums)
    
    
# ----------------------------------------------------

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def moveZeroAtTheEnd(nums):
    
    j = 0
    
    # each time we encounter non-zero element, j is incremented and the element is placed before pivot
    for i in range(len(nums)):
        if nums[i]: # pivot is zero
            swap(nums, i, j)
            j = j + 1
    
if __name__ == "__main__":
    
    nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    moveZeroAtTheEnd(nums)
    print(nums)