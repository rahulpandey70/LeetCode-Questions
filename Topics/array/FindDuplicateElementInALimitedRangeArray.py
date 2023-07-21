"""
    Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, find the duplicate number in it without using any extra space.

    Example:-
    Input:  [1, 2, 3, 4, 4]
    Output: The duplicate element is 4
    
    
    Input:  [1, 2, 3, 4, 2]
    Output: The duplicate element is 2
    
    1. Find the sum of all element and find the difference between it.
    2. For each array element nums[i], invert the sign(positive and negative) of the element present at index nums[i] if it is positive; otherwise, if the element is already negative, then it is a duplicate.
    3. Use hashing to solve this problem. We can use a visited boolean array to mark if an element is seen before or not. If the element is already encountered before, the visited array will return true.

"""

def findDuplicate(nums):
    
    actualSum = sum(nums)
    expectedSum = len(nums) * (len(nums) - 1) // 2
    
    return actualSum - expectedSum

if __name__ == "__main__":
    
    nums = [1, 2, 3, 4, 4]
    print("Duplicate element: ",findDuplicate(nums))
    
# ----------------------------------------------------------------

def findDuplicate(nums):
    
    duplicate = -1
    
    for i in range(len(nums)):
        
        # get the value of the current element
        value = -nums[i] if (nums[i] < 0) else nums[i]
        
        # make element at index value negative if it is positive
        if nums[value] >= 0:
            nums[value] = -nums[value]
        else:
            # if the element is already negative, we found our duplicate
            duplicate = value
            break
    
    for i in range(len(nums)):
        # make negative element positive
        if nums[i] < 0:
            nums[i] = -nums[i]
            
    return duplicate

if __name__ == "__main__":
    
    nums = [1, 2, 3, 4, 4]
    print("Duplicate element: ",findDuplicate(nums))
    
#------------------------------------------------------------------

def findDuplicate(nums):
    
    # initially mark all element false
    visited = [False] * (len(nums) + 1)
    print(visited)
    
    for i in nums:
        
        # check if element is seen before
        if visited[i]:
            return i
        
        # mark visited true
        visited[i] = True
    
    # no duplicate found    
    return -1

if __name__ == "__main__":
    
    nums = [1, 2, 3, 4, 4]
    print("Duplicate element: ",findDuplicate(nums))