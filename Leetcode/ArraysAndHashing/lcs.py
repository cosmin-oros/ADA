# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution(object):
    def longestConsecutive(self, nums):
        # convert the list to a set
        numSet = set(nums)
        lcs = 0

        for n in nums:
            # check if its the start of seq 
            if (n - 1) not in numSet:
                len = 0
                while (n + len) in numSet:
                    len += 1
                lcs = max(len, lcs)

        return lcs


sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums))
