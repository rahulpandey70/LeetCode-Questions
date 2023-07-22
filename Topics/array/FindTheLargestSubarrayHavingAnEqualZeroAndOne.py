"""
    Given a binary array containing 0’s and 1’s, find the largest subarray with equal numbers of 0’s and 1’s.

    Example

    Input:  [0, 0, 1, 0, 1, 0, 0]
    
    Output: [0, 1, 0, 1] or [1, 0, 1, 0]
    
    We can use the map to solve this problem in linear time. Replace 0 with -1 and find out the largest subarray with a sum of 0. To find the largest subarray with a sum of 0, create an empty map that stores the first subarray’s ending index having a given sum. Then traverse the given array and maintain the sum of elements seen so far.

    If the sum is seen for the first time, insert the sum with its index into the map.
    
    If the sum is seen before, there exists a subarray with a sum of 0, which ends at the current index, and update the largest subarray if the current subarray has more length.

"""

def findLargestSubarray(nums):
    
    # create a empty dictionary to store the ending index of first subarray
    d = {}
    
    # insert (0, -1) pair into dictionary
    d[0] = -1
    
    # length store the maximum length of subarray
    length = 0
    
    # store the ending index of the largest subarray
    endingIndex = -1
    
    total = 0
    
    for i in range(len(nums)):
        
        # replace 0 with -1
        total += -1 if (nums[i] == 0) else 1
        
        # check if sum is in dictionary
        if total in d:
            
            # update the length and ending index of largest subarray
            if length < i - d.get(total):
                length = i - d.get(total)
                endingIndex = i 
        
        else:
            d[total] = i

    # print the subarray if any found
    if endingIndex != -1:
        print((endingIndex - length + 1, endingIndex))
    else:
        print("Subarray not found!")
        
if __name__ == "__main__":
    
    nums = [0, 0, 1, 0, 1, 0, 0]
    findLargestSubarray(nums)