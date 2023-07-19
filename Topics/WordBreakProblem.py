"""
    Given a string s and a dictionary of strings wordDict, 
    return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    
    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Example:-

    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code"

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

"""


def wordBreak(self, s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    return dp[0]
