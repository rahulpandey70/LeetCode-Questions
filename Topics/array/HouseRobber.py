"""
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems, 
    connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

    Example:-

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12

"""


def rob(self, nums):
    if len(nums) <= 2:
        return max(nums)

    rob1, rob2 = nums[0], max(nums[0], nums[1])

    for n in nums[2:]:
        temp = max(rob1 + n, rob2)
        rob1, rob2 = rob2, temp  # update both the variables

    return temp  # return the max amount

