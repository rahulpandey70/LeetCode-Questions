"""
Given an integer array, print all subarrays with zero-sum.

Example:-

Input:  { 4, 2, -3, -1, 0, 4 }
 
Subarrays with zero-sum are
 
{ -3, -1, 0, 4 }
{ 0 }
 
 
Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
Subarrays with zero-sum are
 
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

"""
# Brute force approach

def printAllSubarrayWithZeroSum(nums):
    
    # consider all sublists starting from `i`
    for i in range(len(nums)):
        total = 0

        for j in range(i, len(nums)):
            total += nums[j] 

            if total == 0:
                print("SubArray:", (i, j))

if __name__ == "__main__":

    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    printAllSubarrayWithZeroSum(nums)
    

# Using multimap to print all subarray

def insert(d, key, value):
    
    # if the key is in the set map for the first time, initialize the list
    d.setdefault(key, []).append(value)
    
def allSubarrayWithZeroSum(nums):
    
    d = {}
    
    insert(d, 0, -1)
    total = 0
    
    for i in range(len(nums)):
        total = total + nums[i]
        
        if total in d:
            list = d.get(total)
            
            for value in list:
                print("Subarray is", (value + 1, i))
                
        insert(d, total, i)
        
if __name__ == '__main__':
 
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
 
    allSubarrayWithZeroSum(nums)