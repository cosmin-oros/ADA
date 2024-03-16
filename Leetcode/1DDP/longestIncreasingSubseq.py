# Given an integer array nums, return the length of the longest strictly increasing
# subsequence

class Solution(object):
    def lengthOfLIS(self, nums):
        LIS = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(sol.lengthOfLIS(nums))
