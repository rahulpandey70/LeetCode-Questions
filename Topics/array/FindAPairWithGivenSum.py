"""
Find a pair with the given sum in an array.
Given an unsorted integer array, find a pair with the given sum in it.

Example:-
 
Input:

nums = [8, 7, 2, 5, 3, 1]
target = 10
 
Output:
 
Pair found (8, 2)
or
Pair found (7, 3)

Input:

nums = [5, 2, 6, 8, 1, 9]
target = 12
 
Output: Pair not found

"""

# Brute force approach


def findPair(nums, target):

    # Consider each element expect last element
    for i in range(len(nums) - 1):

        # Start the i'th element until the last element
        for j in range(i+1, len(nums)):

            # If desired sum is found
            if nums[i] + nums[j] == target:
                print("Pair found", (nums[i], nums[j]))
                return

    print("Pair not found")


if __name__ == "__main__":

    # nums = [8, 7, 2, 5, 3, 1]
    # target = 10

    # nums = [5, 2, 6, 8, 1, 9]
    # target = 12

    nums = [37, 99, 23, 46]
    target = 60

    findPair(nums, target)

# Time complexity:- o(n^2)
# Space complexity:- o(1)

# -----------------------------------------------------------------------------------

# Using sorting method, where we will maintain to pointers low and high.


def findPair(nums, target):

    # sort the array in ascending order
    nums.sort()

    # maintain two pointer low and high
    low, high = 0, len(nums) - 1

    # loop till the search space is exhausted
    while low < high:
        if nums[low] + nums[high] == target:
            print('Pair found', (nums[low], nums[high]))
            return

        # increment 'low' if the total is less than the desired sum
        # decrement 'high' if the total is more than the desired sum
        if nums[low] + nums[high] < target:
            low += 1
        else:
            high -= 1

    print("Pair not found")


if __name__ == "__main__":

    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    # nums = [5, 2, 6, 8, 1, 9]
    # target = 12

    # nums = [37, 99, 23, 46]
    # target = 60

    findPair(nums, target)

    # Time complexity:- o(n.log(n))
    # Space complexity:- o(1)

#
