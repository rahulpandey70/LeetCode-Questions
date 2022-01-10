"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example:-
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""


def uniquePaths(self, m: int, n: int) -> int:

    path = {}

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1:
                path[(i, j)] = 1
            else:
                path[(i, j)] = path[(i - 1, j)] + path[(i, j - 1)]

    return path[(m, n)]
