"""
    Given an integer array, check if it contains a subarray having zero-sum.
    
    Example:-

    Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
    Output: Subarray with zero-sum exists
    
    The subarrays with a sum of 0 are:
    
    { 3, 4, -7 }
    { 4, -7, 3 }
    { -7, 3, 1, 3 }
    { 3, 1, -4 }
    { 3, 1, 3, 1, -4, -2, -2 }
    { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

    Using hashing we solve this problem, The idea is to use a set to check if a subarray with zero-sum is present in the given array or not. Traverse the array and maintain the sum of elements seen so far. If the sum is seen before (i.e., the sum exists in the set), return true as there exists at least one subarray with zero-sum that ends at the current index; otherwise, insert the sum into the set.
    
"""


def zeroSumSublist(nums):

    # create an empty set to store the sum of elements of each sublist
    s = set()

    # insert 0 into the set to handle the case when sublist with zero sum start from index 0
    s.add(0)
    total = 0

    for i in nums:

        total += i

        # check if the sum is in the set
        if total in s:
            return True

        # add the sum into set
        s.add(total)

    return False


if __name__ == "__main__":

    nums = [4, -6, 3, -1, 4, 2, 7]

    if zeroSumSublist(nums):
        print("Subarray Exists")
    else:
        print("Subarray doesn't exists")

    # Time Complexity:- o(n)
    # Space Complexity:- o(n)