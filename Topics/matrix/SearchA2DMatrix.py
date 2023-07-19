"""
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

    Example:-
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

""" 
def searchMatrix(self, matrix, target) -> bool:
    rows = len(matrix)
    if rows == 0: 
        return False
        
    cols = len(matrix[0])
        
    rStart, rEnd = 0, rows-1
    while rStart < rEnd:
        mid = rStart + (rEnd - rStart) // 2
        if matrix[mid][cols-1] < target: 
            rStart = mid + 1
        elif matrix[mid][0] > target: 
            rEnd = mid - 1
        else:
            rStart = mid
            break
        
    cStart, cEnd = 0, cols - 1
    while cStart <= cEnd:
        mid = cStart + (cEnd - cStart) // 2
        if matrix[rStart][mid] < target: 
            cStart = mid + 1
        elif matrix[rStart][mid] > target: 
            cEnd = mid - 1
        else: 
            return True
        
    return False