"""
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

    Example:-

    Input: x = 123
    Output: 321

    Input: x = -123
    Output: -321

    Input: x = 120
    Output: 21

    Input: x = 0
    Output: 0

"""


def reverseInteger(self, x):
    s = str(abs(x))
    reverseInteger = int(s[::-1])

    if reverseInteger >= 2 ** 31 - 1 or reverseInteger <= -(2 ** 31):
        return 0

    return reverseInteger if x > 0 else (reverseInteger * -1)

