# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        res = 0

        for n in nums:
            res = n ^ res
        return res


nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))