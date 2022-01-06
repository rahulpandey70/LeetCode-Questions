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
