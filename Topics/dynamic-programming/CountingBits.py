"""
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
    ans[i] is the number of 1's in the binary representation of i.

    Example:-

    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

    # Note:- Dp Solution

"""
def countBits(self, n): 
    ans = [0]  # the initial condition
    for i in range(1, n + 1):
        ans.append((i & 1) + ans[i >> 1])  # lastBitof(i) + numberOfOnes(i >> 1)
    return ans