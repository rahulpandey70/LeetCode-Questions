"""
    Given two integers a and b, find the sum of two integers without using + and - .

    Example:-

    Input: a = 1, b = 2
    Output: 3

    Input: a = 2, b = 3
    Output: 5

"""
def getSum(self, a, b):

    # Prevent negative number
    while b & 0xffffffff: # b & 0xffffffff will remain the same as b
        c = a & b
        a = a ^ b
        b = c << 1
        
    return a & 0xffffffff if b > 0xffffffff else a