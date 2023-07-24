"""
    Rearrange an array with alternate high and low elements
    
    Given an integer array, rearrange it such that every second element becomes greater than its left and right elements. Assume no duplicate elements are present in the array.
    
    Example:-
    Input:  [1, 2, 3, 4, 5, 6, 7]
    Output: [1, 3, 2, 5, 4, 7, 6]
    
    Input:  [9, 6, 8, 3, 7]
    Output: [6, 9, 3, 8, 7]
    
    Input:  [6, 9, 2, 5, 1, 4]
    Output: [6, 9, 2, 5, 1, 4]

"""

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def rearrangeArray(nums):
    
    for i in range(1, len(nums), 2):
        
        # if the previous element is greater than the current element swap the elements
        if nums[i - 1] > nums[i]:
            swap(nums, i - 1, i)
        
        # if the next element is greater than the current element swap the elements
        if i + 1 < len(nums) and nums[i + 1] > nums[i]:
            swap(nums, i + 1, i)
    
if __name__ == "__main__":
    
    nums = [6, 9, 2, 5, 1, 4]
    rearrangeArray(nums)
    print(nums)