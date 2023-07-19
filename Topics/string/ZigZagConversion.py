"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

            P   A   H   N
            A P L S I I G
            Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example:-
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "A", numRows = 1
Output: "A"

"""


def convert(self, s: str, numRows: int) -> str:

    if numRows == 1:
        return s

    cycle = 2 * numRows - 2
    res = []
    for i in range(numRows):
        for j in range(i, len(s), cycle):
            res.append(s[j])
            k = j + cycle - 2 * i
            if i != 0 and i != numRows - 1 and k < len(s):
                res.append(s[k])

    return "".join(res)
