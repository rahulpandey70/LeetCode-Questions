"""
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
    Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

    Notice that you may not slant the container.

    Example:-
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input: height = [1,1]
    Output: 1

    Input: height = [4,3,2,1,4]
    Output: 16

    Input: height = [1,2,1]
    Output: 2
    
"""

def mostWater(self, height):

    # Linear time solution O(n)    
    res = 0
    l, r = 0, len(height) - 1
        
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
            
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
                
    return res