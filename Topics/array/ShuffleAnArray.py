"""
    Shuffle an array using Fisher-Yates shuffle algorithm
    
    Given an integer array, in-place shuffle it. The algorithm should produce an unbiased permutation, i.e., every permutation is equally likely.
    
    ```Fisher-Yates shuffle is an algorithm to generate random permutations. It takes time proportional to the total number of items being shuffled and shuffles them in place. The algorithm swaps the element at each iteration at random among all remaining unvisited indices, including the element itself```
    
    To shuffle an array 'a' of 'n' elements (indices 0..n-1):
    for i from n - 1 down to 1 do
       j = random integer with 0 <= j <= i
       exchange a[j] and a[i]

"""
from random import randrange

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def shuffleAnArray(nums):
    
    for i in reversed(range(1, len(nums))):
        # generate a random number j such that 0 <= j <= i
        j = randrange(i + 1)
        
        # swap the current element with randomly generated index
        swap(nums, i, j) 
    
if __name__ == "__main__":
    
    nums = [1, 2, 3, 4, 5, 6]
    shuffleAnArray(nums)
    print("Shuffled array:", nums)
    
# -----------------------------------------------------

from random import randrange

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def shuffleAnArray(nums):
    
    for i in range(len(nums) - 1):
        # generate a random number j such that 0 <= j <= i
        j = randrange(i, len(nums))
        
        # swap the current element with randomly generated index
        swap(nums, i, j) 
    
if __name__ == "__main__":
    
    nums = [1, 2, 3, 4, 5, 6]
    shuffleAnArray(nums)
    print("Shuffled array:", nums)