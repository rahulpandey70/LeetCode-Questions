"""
    A message containing letters from A-Z can be encoded into numbers using the following mapping.

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.

    The answer is guaranteed to fit in a 32-bit integer.

    Example:-

    Input: s = "12"
    Output: 2

    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12)

    Input: s = "226"
    Output: 3
    
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)

    Input: s = "0"
    Output: 0
    
    Explanation: There is no character that is mapped to a number starting with 0.
    The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
    Hence, there are no valid ways to decode this since all digits need to be mapped

    Input: s = "06"
    Output: 0

    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

"""


def numDecode(self, s):
    if len(s) == 0 or s[0] == "0":
        return 0
    if len(s) == 1:
        return 1

    count1, count2 = 1, 1

    for i in range(1, len(s)):
        digit1 = ord(s[i]) - ord("0")
        digit2 = (ord(s[i - 1]) - ord("0")) * 10 + digit1

        count = 0

        if digit1 > 0:
            count += count2
        if digit2 >= 10 and digit2 <= 26:
            count += count1

        count1 = count2
        count2 = count

    return count2
