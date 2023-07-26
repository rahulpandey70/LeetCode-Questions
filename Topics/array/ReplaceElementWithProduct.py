"""
    Replace every array element with the product of every other(expect itself) element without using a division operator
    
    Given an integer array, replace each element with the product of every other element without using the division operator.
    
    Example:
    
    Input:  [1, 2, 3, 4, 5]
    Output: [120, 60, 40, 30, 24]
    
    
    Input:  [5, 3, 4, 2, 6, 8]
    Output: [1152, 1920, 1440, 2880, 960, 720]

"""

def findProduct(nums, n, left = 1, i = 0):
    
    # base case
    if i == n:
        return 1
    
    # current element
    curr = nums[i]
    
    # calculate the product of right subarray
    right = findProduct(nums, n, left * nums[i], i + 1)
    
    # replace the current element with the product of left and right subarray
    nums[i] = left * right
    
    # return product of right the subarray, including the current element
    return curr * right
    
if __name__ == "__main__":
    
    nums = [5, 3, 4, 2, 6, 8]
    findProduct(nums, len(nums))
    
    print(nums)