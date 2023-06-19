# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # keep track of the count of each character in s1 and s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            # get the ascii value with ord
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s1[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # left index of the sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            # check if all the characters in s1 have been matched
            if matches == 26:
                return True

            # add character to the right of the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # same thing but to the left
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))
