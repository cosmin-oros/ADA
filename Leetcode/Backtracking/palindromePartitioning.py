# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.

class Solution(object):
    def partition(self, s):
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l, r = l + 1, r - 1
        return True


s = "aab"
sol = Solution()
print(sol.partition(s))