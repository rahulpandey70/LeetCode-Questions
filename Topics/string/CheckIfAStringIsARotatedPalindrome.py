"""
    Given a string, check if it is a rotated palindrome or not.

    Example,

    CBAABCD is a rotated palindrome as it is a rotation of palindrome ABCDCBA.
    BAABCC is a rotated palindrome as it is a rotation of palindrome ABCCBA.
    
    1. A brute solution is to consider all rotations of the given string and check if any rotation is a palindrome or not. If we have found a rotation that is a palindrome, return true; otherwise, return false.

"""

def isPalindrome(s, low, high):
    return (low >= high) or (s[low] == s[high] and isPalindrome(s, low + 1, high - 1))

def isRotatedPalindrome(s):
    
    n = len(s)
    
    for i in range(n):
        
        # in-place rotate the string by 1 unit
        s = s[1:] + s[0]
        
        # return true if rotation is a palindrome
        if isPalindrome(s, 0, n - 1):
            return True
        
    return False
    
if __name__ == "__main__":
    
    s = "ABCDCBA"
    
    # rotate it, by 2 units
    s = s[2:] + s[:2]
    
    if isRotatedPalindrome(s):
        print("String is a rotated palindrome")
    else:
        print("String is not a rotated palindrome")
     