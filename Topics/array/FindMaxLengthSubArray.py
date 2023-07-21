"""
    Given an integer array, find the maximum length subarray having a given sum.

    Example:-
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
    
    Subarrays with sum 8 are
    
    { -5, 5, 3, 5 }
    { 3, 5 }
    { 5, 3 }
    
    The longest subarray is { -5, 5, 3, 5 } having length 4.
    
    1. A brute force solution is to consider all subarrays and find their sum. If the subarray sum is equal to the given sum, update the maximum length subarray. The time complexity of the naive solution is O(n3) as there are n2 subarrays in an array of size n, and it takes O(n) time to find the sum of its elements. We can optimize the method to run in O(n2) time by calculating the subarray sum in constant time
    
    2. We can use a map to solve this problem in linear time. The idea is to create an empty map to store the first subarray’s ending index, having a given sum. We traverse the given array and maintain the sum of elements seen so far.

    If the target is seen for the first time, insert the sum with its index into the map.
    
    If target-S is seen before, there is a subarray with the given sum that ends at the current index, and we update the maximum length subarray having sum S if the current subarray has more length.

"""

def findMaxLengthSubarray(nums, s):
    
    # store the maximum length of subarray with sum s
    length = 0
    
    # store ending index of the maximum length subarray having sum s
    endingIndex = -1
    
    for i in range(len(nums)):
        target = 0
        for j in range(i, len(nums)):
            
            target += nums[j]

            if target == s:
                
                # update the length and endingIndex of maximum length subarray
                if length < j - i + 1:
                    length = j - i + 1
                    endingIndex = j
                    
    # print subarray
    print((endingIndex - length + 1, endingIndex))
    
if __name__ == "__main__":
    
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8 
    
    findMaxLengthSubarray(nums, target)
    
# -------------------------------------------------------------

def findMaxLengthSubarray(nums, s):
    
    # create empty dictionary to store the ending index of the first subarray
    d = {}
    
    # insert (0, -1) pair into dictionary to handle the case when a subarray with sum 's' start from index 0. 
    d[0] = -1
    
    target = 0
    length = 0
    endingIndex = -1
    
    for i in range(len(nums)):
        
        target += nums[i]
        
        # check if the sum is not dictionary, insert it into dictionary
        if target not in d:
            d[target] = i
        
        # update the length and endingIndex of the maximum length subarray having sum `s`
        if target - s in d and length < i - d[target - s]:
            length = i - d[target - s]
            endingIndex = i    
    
    # print subarray
    print((endingIndex - length + 1, endingIndex))
    
if __name__ == "__main__":
    
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8 
    
    findMaxLengthSubarray(nums, target)