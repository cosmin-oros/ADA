# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


s = "leetcode"
wordDict = ["leet", "code"]
sol = Solution()
print(sol.wordBreak(s, wordDict))