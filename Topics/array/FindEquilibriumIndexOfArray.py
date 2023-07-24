"""
    Given an integer array, find the equilibrium index in it.

    Example:-
    
    a = [-7, 1, 5, 2, -4, 3, 0]
    
    output = 3
    
    a[0] + a[1] + a[2] = a[4] + a[5] + a[6] = -1
    -7 + 1 + 5 = -4 + 3 + 0
    -1 = -1
    
    ---------------------------------
    
    a = [0, 1, 3, -2, -1] 
    
    output = 1
    
    a[0] = a[2] + a[3] + a[4]
    0 = 3 + (-2) + (-1)
    0 = 0
    
    ---------------------------------
    
    a = [1, 2, -2, -1]
    
    output = -1 (no such equilibrium index)
    
    a[0] + a[1] = a[2] + a[3]
    1 + 2 = (-2) + (-1)
    3 = 3

"""

def equilibriumIndex(a, n):
    
    totalSum = 0
    leftSum = 0
    
    for i in range(n):
        totalSum = totalSum + a[i]
        
    for i in range(n):
        rightSum = totalSum - leftSum - a[i]
        
        if leftSum == rightSum:
            return i
        
        leftSum = leftSum + a[i]
        
    return -1
    
if __name__ == "__main__":
    a = [-7, 1, 5, 2, -4, 3, 0]
    n = len(a)
    
    print(equilibriumIndex(a, n))