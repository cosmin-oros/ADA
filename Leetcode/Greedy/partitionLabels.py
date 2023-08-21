# You are given a string s. We want to partition the string into as many parts as possible so that each letter
# appears in at most one part.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts.

class Solution(object):
    def partitionLabels(self, s):
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            if i == end:
                res.append(size)
                size = 0
        return res


s = "ababcbacadefegdehijhklij"
sol = Solution()
print(sol.partitionLabels(s))