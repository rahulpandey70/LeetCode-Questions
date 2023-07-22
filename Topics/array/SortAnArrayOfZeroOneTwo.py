"""
    Given an array containing only 0's, 1's, and 2's, sort it in linear time and using constant space.(Dutch National Flag Problem)

    Example:
    
    Input:  [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

    We can rearrange the array in a single traversal using an alternative linear-time partition routine that separates the values into three groups:

    The values less than the pivot,
    The values equal to the pivot, and
    The values greater than the pivot.

"""

def swap(nums, i, j):
    
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def rearrangeArray(nums):
    
    start = mid = 0
    pivot = 1
    end = len(nums) - 1
    
    while mid <= end:
        
        # current element is 0
        if nums[mid] < pivot:
            swap(nums, start, mid)
            start = start + 1
            mid = mid + 1
        # current element is 2
        elif nums[mid] > pivot:
            swap(nums, mid, end)
            end = end - 1
        
        # current element is 1
        else:
            mid = mid + 1
            
if __name__ == "__main__":
    
    nums = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    rearrangeArray(nums)
    print(nums)