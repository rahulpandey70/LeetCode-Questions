"""
    Given a binary array, find the index of 0 to be replaced with 1 to get the maximum length sequence of continuous ones.

    For example, consider the array [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]. We need to replace index 7 to get the continuous sequence of length 6 containing all 1's.

"""

def findZeroIndex(nums):
    
    maxCount = 0 # store maximum number of 1's(including 0's)
    maxIndex = -1 # store index of 0 to be replaced
    
    prevZeroIndex = -1 # store index of previous zero
    count = 0 # store current count of zero
    
    for i in range(len(nums)):
        
        # check if the current element is 1
        if nums[i] == 1:
            count = count + 1
            print("if block count", count)
        else:
            # if the current element is 0, reset count to 1 + number of ones to the left of current 0
            count = i - prevZeroIndex
            print("else block count", count)
            
            # update previous count to current index
            prevZeroIndex = i
            print("zero index", prevZeroIndex)
        
        # update maximum count and index of 0 to be replaced if required
        if count > maxCount:
            maxCount = count
            maxIndex = prevZeroIndex
            print("max index", maxIndex)
    
    return maxIndex 
    
    
if __name__ == "__main__":
    
    nums = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    index = findZeroIndex(nums)
    
    if index != -1:
        print("Index to be replaced is", index)
    else:
        print("Invalid input")