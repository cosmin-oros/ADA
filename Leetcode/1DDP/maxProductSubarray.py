# Given an integer array nums, find a
# subarray
#  that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            t = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(t, n * curMin, n)
            res = max(res, curMax)
        return res


nums = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProduct(nums))
