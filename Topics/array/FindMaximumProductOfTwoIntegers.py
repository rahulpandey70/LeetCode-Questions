"""
    Given an integer array, find the maximum product of two integers in it.

    Example:-
    array = [-10, -3, 5, 6, -2]
    The maximum product is the (-10, -3) or (5, 6) pair.
    
    1. A brute force solution is to consider every pair of elements and calculate their product. Update the maximum product found so far if the product of the current pair is greater. Finally, print the elements involved in the maximum product.
    
    2. The time complexity can be improved by sorting the array. Then the result is the maximum of the following:

    The product of maximum and second maximum integer in the array (i.e., the last two elements in a sorted array).
    
    The product of minimum and second minimum integers in the array (i.e., the first two elements in the sorted array).

"""
import sys

def findMaximumProduct(nums):
    
    # base case
    if len(nums) < 2:
        return

    maxProduct = -sys.maxsize
    max_i = max_j = -1
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            
            # update the maximum product
            if maxProduct < nums[i] * nums[j]:
                maxProduct = nums[i] * nums[j]
                (max_i, max_j) = (i, j)
    
    print("Pair is: ", (nums[max_i], nums[max_j]))
    
if __name__ == "__main__":
    
    nums = [-10, -3, 5, 6, -2]
    findMaximumProduct(nums)
    
#-------------------------------------------------------------

def findMaximumProduct(nums):
    
    length = len(nums)
    
    # base case
    if length < 2:
        return

    # sort the array
    nums.sort()
    
    if (nums[0] * nums[1]) > (nums[length - 1] * nums[length - 2]):
        print("Pair is: ", (nums[0], nums[1]))
    else:
        print("Pair is: ", (nums[length - 1], nums[length - 2]))
        
    
if __name__ == "__main__":
    
    nums = [-10, -3, 5, 6, -2]
    findMaximumProduct(nums)