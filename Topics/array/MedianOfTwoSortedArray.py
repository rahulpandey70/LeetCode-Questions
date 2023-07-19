"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    Example:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    
"""

def findMedianSortedArrays(self, nums1, nums2):
    lst = nums1 + nums2
    if lst == []:
        return 0
    lst = sorted(lst)
    median = len(lst) // 2
    if len(lst)%2 !=0:
        return lst[median]
    else:
        return (lst[median] + lst[median-1]) / 2