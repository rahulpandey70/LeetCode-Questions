"""
    Find majority element (Boyer-Moore Majority Vote Algorithm)

    Given an integer array containing duplicates, return the majority element if present. A majority element appears more than n/2 times, where n is the array size.

    Example:-
    
    arr = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
    
    The majority element is 2 in array.

"""

def findMajorityElement(nums):
    
    # empty dictionary
    d = {}
    
    # store each element frequency in a dictionary
    for i in nums:
        d[i] = d.get(i, 0) + 1
        
    # return the element if its count is more than n/2
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    
    # no majority element found
    return -1
    
if __name__ == "__main__":
    
    nums = [2, 8, 7, 2, 2, 5, 2, 3, 1]
    majority = findMajorityElement(nums)
    
    print("Majority element is:", majority)
    
#-----------------------------------------------------

def findMajorityElement(nums):
    
    # store the majority element
    m = -1
    
    # counter
    i = 0
    
    for j in range(len(nums)):
        
        if i == 0:
            m = nums[j]
            i = 1
            
        elif m == nums[j]:
            i = i + 1
            
        else:
            i = i - 1
            
    return m
    
if __name__ == "__main__":
    
    nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
    majority = findMajorityElement(nums)
    
    print("Majority element is:", majority)