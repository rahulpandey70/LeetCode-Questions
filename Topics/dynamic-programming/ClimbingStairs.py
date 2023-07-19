"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example:-

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

"""

def climbStairs(self, n):
    """
    In this problem initilize last two number with one and then add both of them to find 3rd last number,
    and then shift our both number to right and continue this process. Just like fibonacci series.    
    """
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
        
    return one