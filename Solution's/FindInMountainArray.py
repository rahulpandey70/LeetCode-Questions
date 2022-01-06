"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, 
return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).

MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.Also, 
any solutions that attempt to circumvent the judge will result in disqualification.

Example:-

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1

"""


def findInMountainArray(self, target, mountain_arr):
    peak = self.peekElement(mountain_arr)
    firsttry = self.binarySearch(mountain_arr, target, 0, peak)
    if firsttry != -1:
        return firsttry
    return self.binarySearch(mountain_arr, target, peak + 1, mountain_arr.length() - 1)


# Find the peek element of the array
def peekElement(self, mountain_arr):
    start = 0
    end = mountain_arr.length() - 1

    while start < end:
        mid = start + (end - start) // 2
        if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
            end = mid
        else:
            start = mid + 1
    return start


# Normal binary search
def binarySearch(self, mountain_arr, target, start, end):

    is_asc = mountain_arr.get(start) < mountain_arr.get(end)

    while start <= end:
        mid = (start + end) // 2
        if mountain_arr.get(mid) == target:
            return mid
        if is_asc:
            if target < mountain_arr.get(mid):
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > mountain_arr.get(mid):
                end = mid - 1
            else:
                start = mid + 1
    return -1
