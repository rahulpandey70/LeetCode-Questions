"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Example:-

    Input: nums = [1,2,3,1]
    Output: true

    Input: nums = [1,2,3,4]
    Output: false

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

"""

def containsDuplicate(self, nums):
    return len(set(nums)) != len(nums)
    """
    Basically checking non-repeating(set only returns non repeating numbers) array is equal to repeating array.
    """