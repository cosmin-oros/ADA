# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # a - z

            for c in s:
                # ord - ascii value
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
    # O(m * n)


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))