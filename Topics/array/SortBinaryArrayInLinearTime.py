"""
Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

Mean's that time complexity should be o(n) and space complexity should be o(1).

Example:-

Input:  [1, 0, 1, 0, 1, 0, 0, 1]
 
Output: [0, 0, 0, 0, 1, 1, 1, 1]

1. Count the total number of 0's present in the array, say k, and fill the first k indices  in the array by 0 and all remaining indices by 1.

2. If the current element is 0, we can place 0 at the next available position in the array. After all elements in the array are processed, we fill all remaining indices by 1.

3. We can also solve this problem in linear time by using the partitioning logic of Quicksort. The idea is to use 1 as a pivot element and make one pass of the partition process. The resultant array will be sorted

"""

def sortBinaryArray(nums):
    
    # count number of 0's in array
    zeros = nums.count(0)
    
    # put 0's at the beginning
    k = 0
    while zeros:
        nums[k] = 0
        zeros = zeros - 1
        k = k + 1
    
    # fill all the remaining elements by 1
    for k in range(k, len(nums)):
        nums[k] = 1
        
if __name__ == "__main__":
    
    nums = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    
    sortBinaryArray(nums)
    print(nums)
    
    # Time complexity:- o(n)
    # Space complexity:- o(1)
    
    
# --------------------------------------------------------------------

def sortBinaryArray(nums):
    
    # stores index of next available position
    k = 0
    for i in range(len(nums)):
        
        # check if the current element is zero, place 0 at the next position
        if nums[i] == 0:
            nums[k] = 0
            k = k + 1
        
    # fill all remaining position by 1.
    for i in range(k, len(nums)):
        nums[k] = 1
        k = k + 1
        
if __name__ == "__main__":
    
    nums = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    
    sortBinaryArray(nums)
    print(nums)
    
    # Time complexity:- o(n)
    # Space complexity:- o(1)
    
# ----------------------------------------------------------------------

def sortBinaryArray(nums):
    
    pivot = 1
    k = 0
    
    # Each time we find 0, k is incremented, and place 0 before pivot
    for i in range(len(nums)):
        if nums[i] < pivot:
            swap(nums, i, k)
            k = k + 1
    
def swap(nums, i, k):
    temp = nums[i]
    nums[i] = nums[k]
    nums[k] = temp
        
if __name__ == "__main__":
    
    nums = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    
    sortBinaryArray(nums)
    print(nums)