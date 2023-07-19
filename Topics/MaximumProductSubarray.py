"""
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
    and return the product.

    It is guaranteed that the answer will fit in a 32-bit integer.
    
    A subarray is a contiguous subsequence of the array.

    Example:-
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


def maxProduct(self, nums):
    max_overall = nums[0]
    max_ending, min_ending = nums[0], nums[0]

    for i in range(1, len(nums)):
        temp = max_ending
        max_ending = max({nums[i], nums[i] * max_ending, nums[i] * min_ending})
        min_ending = min({nums[i], nums[i] * temp, nums[i] * min_ending})
        max_overall = max(max_overall, max_ending)

    return max_overall
